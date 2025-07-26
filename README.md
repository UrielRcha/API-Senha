# Gerador de Login e Senha Seguros — API Flask

![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Flask](https://img.shields.io/badge/Flask-1.1.2-green) ![License](https://img.shields.io/badge/license-MIT-lightgrey)

## Descrição

API simples construída com Flask para gerar **logins** e **senhas seguras** de forma dinâmica, com parâmetros personalizáveis para o tamanho das strings. Ideal para automação de cadastros, testes ou aplicações que demandem credenciais temporárias e seguras.

---

## Funcionalidades

- Gera logins aleatórios com letras, números e caracteres especiais.
- Gera senhas fortes, com pelo menos uma letra minúscula, uma maiúscula, um número e um caractere especial.
- Parâmetro opcional para definir o tamanho do login ou senha.
- Validação mínima do tamanho (login ≥ 4 caracteres, senha ≥ 8 caracteres).
- API RESTful simples com endpoints GET.

---

## Endpoints

### Gerar Senha

- Parâmetro `tamanho` (opcional): inteiro, mínimo 8. Define o comprimento da senha.
- Retorna JSON com a senha gerada.
- Exemplo de resposta:

```json
{
  "senha": "aB3$7fGh!2kLmnOp"
}
```
- Em caso de erro, retorna status 400 com mensagem descritiva.
---

### Endpoints

### Gerar Logins
- Parâmetro `tamanho` (opcional): inteiro, mínimo 4. Define o comprimento do login.
- Retorna JSON com o login gerado.
- Exemplo de resposta:

```json
{
  "login": "A9f#7H2p"
}
```
- Em caso de erro, retorna status 400 com mensagem descritiva.
- Permite requisições CORS (Cross-Origin Resource Sharing).
---
### Endpoints

### Como usar
1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/gerador-login-senha.git
cd gerador-login-senha
```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
3. Instale as dependências:
```bash
pip install flask
```
4. Execute a aplicação:
```bash
python app.py
```

## Contribuição
- Pull requests e issues são bem-vindos! Sinta-se à vontade para sugerir melhorias ou reportar bugs.

