from flask import Flask, jsonify, render_template, Response
from requests.api import post, request
from flask_restful import Api, Resource, abort, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import json, mysql.connector


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=True)


note_post_args = reqparse.RequestParser()
note_post_args.add_argument('title', type=str, help='Title is required', required=True)
note_post_args.add_argument('description', type=str, required=False)
note_post_args.add_argument('date', type=str, required=True)

note_put_args = reqparse.RequestParser()
note_put_args.add_argument('title', type=str, help='Title is required', required=True)
note_put_args.add_argument('description', type=str, required=False)
note_put_args.add_argument('date', type=str, required=True)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello():
    return 'Hello World!'

@app.route('/nota/<id>', methods=['GET'])
def selecionar_nota():
    return
@app.route('/nota', methods=['POST'])
def criar_nota():
    return
@app.route('/nota/<id>', methods=['PUT'])
def editar_nota():
    return

@app.route('/nota/<id>', methods=['DELETE'])
def excluir_nota():
    return

if __name__ == "__main__":
    app.run(debug=True)