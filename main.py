from flask import Flask, jsonify
from flask.globals import request
from data import json_object


app = Flask(__name__)
@app.route('/anotacoes')
def delete():
    return delete
@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    return jsonify({"About":"hello world"})
    

@app.route('/get/<text>', methods=['GET'])
def criar_nota(text):
    return jsonify({
        "title":text,
        "date": 2021,
        "description": "Ok",
        "id": 0})
@app.route('/post/<data>', methods=['POST'])
def editar_nota(data):
    return jsonify({
        'title': data,
        'date': 2021,
        'description': 'Ok',
        'id': 0
    })
if __name__ == "__main__":
    app.run(debug=True)