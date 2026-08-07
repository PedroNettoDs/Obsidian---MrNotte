É um [[Banco de dados Vetorial]], leve e focado em aplicações de [[Inteligência Artificial|IA]] com [[RAG - Retrieval-Augmented Generation]], ideal para buscas semânticas locais 

diferente de um banco de dados que você procura por 'nome de coluna', no vetorial, ele busca por 'semântica' (palavras semelhantes).

Para isso, suas documentações precisam passar por uma [[Indexação]], transformando cada texto em um vetor.

Quem faz essa transformação é o [[nomic-embed-text]] rodando em conjunto do [[Ollama]].

A cada 'pergunta/consulta' vira também um vetor