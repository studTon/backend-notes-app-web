from flask import Flask, jsonify, render_template, Response, request
from flask_sqlalchemy import SQLAlchemy
import requests, json, mysql.connector

resposta = 0
app = Flask(__name__)
@app.route('/anotacoes')
def delete():
    return delete
@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello():
    return 'hello world'

@app.route('/get', methods=['GET'])
def criar_nota():
    resposta = requests.get()
    return resposta
@app.route('/post', methods=['POST'])
def salvar_nota():
    resposta = requests.post()

@app.route('/put', methods=['PUT'])
def editar_nota():
    resposta = requests.put()

@app.route('/delete', methods=['DELETE'])
def excluir_nota():
    resposta = requests.delete()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost'

db = SQLAlchemy(app)

class Note(db.Model):
    title = db.Column(db.String(50), primary_key=True)
    description = db.Column(db.String(100))
    id = db.Column(db.Integer)
    #date = db.Column(db.Date)



if __name__ == "__main__":
    app.run(debug=True)