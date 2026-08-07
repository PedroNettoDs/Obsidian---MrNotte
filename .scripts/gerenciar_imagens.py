#!/usr/bin/env python3
"""Encontra/limpa imagens órfãs em /midias e permite embuti-las como base64 direto nas notas."""

import argparse
import base64
import io
import os
import re
import sys
import unicodedata
import urllib.parse
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent
MIDIAS_DIR = VAULT_ROOT / "midias"
LIXEIRA_DIR = MIDIAS_DIR / "_lixeira"

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp"}
IGNORED_DIRS = {".git", ".obsidian", ".smart-env", ".trash", "_lixeira"}

EMBED_RE = re.compile(r"!\[\[([^\]]+)\]\]")
MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")


def iter_markdown_files():
    for dirpath, dirnames, filenames in os.walk(VAULT_ROOT):
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]
        for name in filenames:
            if name.endswith(".md"):
                yield Path(dirpath) / name


def normalize(name: str) -> str:
    return unicodedata.normalize("NFC", name.strip())


def extract_local_references() -> set:
    referenced = set()
    for md_path in iter_markdown_files():
        text = md_path.read_text(encoding="utf-8", errors="ignore")
        for match in EMBED_RE.findall(text):
            candidate = re.split(r"\\?\|", match, maxsplit=1)[0].strip()
            candidate = os.path.basename(candidate)
            if candidate:
                referenced.add(normalize(candidate))
        for match in MD_IMAGE_RE.findall(text):
            candidate = os.path.basename(urllib.parse.unquote(match.strip()))
            if candidate:
                referenced.add(normalize(candidate))
    return referenced


def iter_midias_images():
    for dirpath, dirnames, filenames in os.walk(MIDIAS_DIR):
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]
        for name in filenames:
            if Path(name).suffix.lower() in IMAGE_EXTS:
                yield Path(dirpath) / name


def caminho_livre(destino: Path) -> Path:
    if not destino.exists():
        return destino
    stem, suf = destino.stem, destino.suffix
    i = 1
    while True:
        alt = destino.with_name(f"{stem} ({i}){suf}")
        if not alt.exists():
            return alt
        i += 1


def cmd_limpar(args):
    referenced = extract_local_references()
    imagens = list(iter_midias_images())
    orfas_locais = [img for img in imagens if normalize(img.name) not in referenced]

    total_bytes = sum(f.stat().st_size for f in orfas_locais)

    print(f"Imagens em /midias: {len(imagens)}")
    print(f"Referenciadas: {len(imagens) - len(orfas_locais)}")
    print(f"Órfãs locais: {len(orfas_locais)} ({total_bytes / 1024:.1f} KB)")
    for img in orfas_locais:
        print(f"  - {img.relative_to(VAULT_ROOT)}")

    if not orfas_locais:
        print("\nNada para limpar.")
        return

    if not args.apply:
        print("\nModo dry-run (padrão). Rode novamente com --apply para mover o que foi listado acima para midias/_lixeira/.")
        return

    LIXEIRA_DIR.mkdir(parents=True, exist_ok=True)
    for img in orfas_locais:
        destino = caminho_livre(LIXEIRA_DIR / img.name)
        img.rename(destino)
        print(f"Movido: {img.relative_to(VAULT_ROOT)} -> {destino.relative_to(VAULT_ROOT)}")


def find_image_file(nome: str) -> Path:
    alvo = normalize(os.path.basename(nome))
    encontrados = [img for img in iter_midias_images() if normalize(img.name) == alvo]
    if not encontrados:
        print(f"Imagem não encontrada em /midias: {nome}")
        sys.exit(1)
    if len(encontrados) > 1:
        print(f"Mais de um arquivo chamado '{alvo}' encontrado, use o caminho completo para desempatar:")
        for f in encontrados:
            print(f"  - {f.relative_to(VAULT_ROOT)}")
        sys.exit(1)
    return encontrados[0]


def compress_to_webp_base64(caminho: Path, largura_maxima: int, qualidade: int, lossless: bool):
    try:
        from PIL import Image
    except ImportError:
        print("Pillow não está instalado. Rode: pip install pillow")
        sys.exit(1)

    with Image.open(caminho) as img:
        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGBA" if "A" in img.getbands() else "RGB")
        if img.width > largura_maxima:
            nova_altura = round(img.height * largura_maxima / img.width)
            img = img.resize((largura_maxima, nova_altura), Image.Resampling.LANCZOS)
        buffer = io.BytesIO()
        img.save(buffer, format="WEBP", quality=qualidade, lossless=lossless, method=6)
        dados = buffer.getvalue()

    return base64.b64encode(dados).decode("ascii"), len(dados)


def replace_embeds_with_data_uri(basename: str, data_uri: str) -> list:
    pattern = re.compile(r"!\[\[" + re.escape(basename) + r"(?:\s*\\?\|\s*([^\]]*))?\]\]")
    alteradas = []
    for md_path in iter_markdown_files():
        texto = md_path.read_text(encoding="utf-8", errors="ignore")
        if not pattern.search(texto):
            continue

        def substituir(m):
            tamanho = m.group(1)
            alt = f"|{tamanho.strip()}" if tamanho else ""
            return f"![{alt}]({data_uri})"

        novo_texto = pattern.sub(substituir, texto)
        md_path.write_text(novo_texto, encoding="utf-8")
        alteradas.append(md_path)
    return alteradas


def cmd_embutir(args):
    if args.todas:
        alvo = list(iter_midias_images())
    else:
        if not args.imagem:
            print("Informe o nome de uma imagem ou use --todas.")
            sys.exit(1)
        alvo = [find_image_file(args.imagem)]

    notas_tocadas = set()
    total_original = total_base64 = 0
    sem_referencia = []
    maior_que_original = []
    falhas = []

    for caminho in alvo:
        tamanho_original = caminho.stat().st_size
        try:
            b64, _ = compress_to_webp_base64(
                caminho, args.largura_maxima, args.qualidade, args.lossless
            )
        except Exception as e:
            falhas.append((caminho, str(e)))
            continue

        if len(b64) >= tamanho_original:
            maior_que_original.append(caminho)
            continue

        data_uri = f"data:image/webp;base64,{b64}"
        alteradas = replace_embeds_with_data_uri(caminho.name, data_uri)

        if not alteradas:
            sem_referencia.append(caminho)
            continue

        total_original += tamanho_original
        total_base64 += len(b64)
        notas_tocadas.update(alteradas)
        print(f"{caminho.relative_to(VAULT_ROOT)}: {tamanho_original / 1024:.1f} KB -> {len(b64) / 1024:.1f} KB base64 ({len(alteradas)} nota(s))")

    if notas_tocadas:
        print(f"\nTotal: {len(notas_tocadas)} nota(s) atualizadas, {total_original / 1024:.1f} KB originais -> {total_base64 / 1024:.1f} KB em base64.")
        print("Os arquivos originais continuam em /midias. Rode 'limpar' quando quiser mover os que ficaram órfãos para _lixeira.")
    if sem_referencia:
        print(f"\n{len(sem_referencia)} imagem(ns) sem referência ![[...]] em nenhuma nota, ignoradas: {', '.join(i.name for i in sem_referencia)}")
    if maior_que_original:
        print(f"\n{len(maior_que_original)} imagem(ns) ficariam maiores em base64 do que o original, ignoradas: {', '.join(i.name for i in maior_que_original)}")
    if falhas:
        print(f"\n{len(falhas)} imagem(ns) falharam ao processar:")
        for caminho, erro in falhas:
            print(f"  - {caminho.relative_to(VAULT_ROOT)}: {erro}")
    if not (notas_tocadas or sem_referencia or maior_que_original or falhas):
        print("Nada para fazer.")


def main():
    parser = argparse.ArgumentParser(description="Gerencia imagens órfãs em /midias e permite embuti-las como base64.")
    sub = parser.add_subparsers(dest="comando", required=True)

    p_limpar = sub.add_parser("limpar", help="Lista (ou move com --apply) imagens órfãs para midias/_lixeira/.")
    p_limpar.add_argument("--apply", action="store_true", help="Move de fato em vez de só listar.")
    p_limpar.set_defaults(func=cmd_limpar)

    p_embutir = sub.add_parser("embutir", help="Comprime uma imagem e a embute como base64 nas notas que a referenciam.")
    p_embutir.add_argument("imagem", nargs="?", help="Nome ou caminho da imagem dentro de /midias (omita se usar --todas).")
    p_embutir.add_argument("--todas", action="store_true", help="Aplica em todas as imagens de /midias que tiverem referência em alguma nota.")
    p_embutir.add_argument("--largura-maxima", type=int, default=1600, dest="largura_maxima", help="Redimensiona se a imagem for mais larga que isso (padrão: 1600px).")
    p_embutir.add_argument("--qualidade", type=int, default=80, help="Qualidade do WebP, 0-100 (padrão: 80).")
    p_embutir.add_argument("--lossless", action="store_true", help="Usa WebP sem perdas (melhor para screenshots com texto fino).")
    p_embutir.set_defaults(func=cmd_embutir)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
