from logging import error
from typing import get_args
from flask import Flask, jsonify, json
from flask.globals import request


app = Flask(__name__)
@app.route('/anotacoes')
def lista_anotacoes():
    
    lista_notas = []
    for i in range(0, 2):
        dicion_notas = {
            "date": 2021,
            "title": "Nota 1" ,
            "description": "Ok",
            "id": 2,
        }
        lista_notas.append(dicion_notas)

        jsonStr = json.dumps(lista_notas)

    return True
def delete():
    return delete
@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    if (request.method == 'POST'):
        nota = request.get_json()
        return jsonify({}), 201
    elif (request.method == 'GET'):
        return jsonify({"about":"hello world"})
    elif (request.method == 'PUT'):
        edit = request.get_json()
        return jsonify({edit}), 202
    else:
        return delete, 203

@app.route('/<text>', methods=['GET'])
def criar_nota(text):
    return jsonify({'Texto':text})

if __name__ == "__main__":
    app.run(debug=True)