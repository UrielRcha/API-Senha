from flask import Flask, jsonify, request
import secrets
import string
import random

app = Flask(__name__)

def caracteres_validos():
    return string.ascii_letters + string.digits + "!@#$%^&*()-_=+"


def gerar_login(tamanho=8):
    caracteres = caracteres_validos()
    login = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return login

def gerar_senha(tamanho=16):
    if tamanho < 8:  
        raise ValueError("O tamanho deve ser pelo menos 8 caracteres")

    caracteres = caracteres_validos()
    
    senha = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice("!@#$%^&*()-_=+")
    ]
    
    senha += [secrets.choice(caracteres) for _ in range(tamanho - 4)]
    secrets.shuffle(senha)
    
    return ''.join(senha)

@app.route('/gerar_senha', methods=['GET'])
def senha_api():
    try:
        tamanho = int(request.args.get('tamanho', default=16))
        
        if tamanho < 8:
            return jsonify({"erro": "O tamanho da senha deve ser no mínimo 8 caracteres"}), 400
        
        senha_segura = gerar_senha(tamanho)
        return jsonify({"senha": senha_segura})
    
    except ValueError:
        return jsonify({"erro": "O parâmetro 'tamanho' deve ser um número inteiro válido"}), 400

@app.route('/gerar_login', methods=['GET'])
def login_api():
    tamanho = request.args.get('tamanho', default=8, type=int)

    if tamanho < 4:
        return jsonify({"erro": "O login deve ter no mínimo 4 caracteres"}), 400

    login_gerado = gerar_login(tamanho)

    resposta = jsonify({"login": login_gerado})
    resposta.headers.add("Access-Control-Allow-Origin", "*")  # Permite CORS
    return resposta

if __name__ == '__main__':
    app.run(debug=True)
