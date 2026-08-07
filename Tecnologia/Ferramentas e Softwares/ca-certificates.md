conjunto de **certificados raiz de Autoridades Certificadoras (CAs)** confiáveis pelo sistema.

Na prática, isso permite que o sistema:

- Confie em conexões **[[HTTPS (Hypertext Transfer Protocol Secure)]]/[TLS]()**    
- Valide certificados de sites como:    
    - `https://download.docker.com`
    - `https://security.ubuntu.com`
        
- Evite erros do tipo:
```
SSL certificate problem: unable to get local issuer certificate
```
    
Sem esse pacote, downloads HTTPS podem **falhar ou ser inseguros**.

---