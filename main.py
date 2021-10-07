from flask import Flask, jsonify, render_template, Response
from requests.api import post, request
from flask_restful import Api, Resource, abort, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import json, mysql.connector

resposta = 0
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=True)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello():
    return 'Hello World!'

@app.route('/nota/<id>', methods=['GET'])
def selecionar_nota():

@app.route('/nota', methods=['POST'])
def criar_nota():
args = nota.parse_args()
@app.route('/nota/<id>', methods=['PUT'])
def editar_nota():
    

@app.route('/nota/<id>', methods=['DELETE'])
def excluir_nota():
    

if __name__ == "__main__":
    app.run(debug=True)