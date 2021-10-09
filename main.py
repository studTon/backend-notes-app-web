from flask import Flask, jsonify, render_template, Response
from requests.api import post, request
from flask_restful import Api, Resource, abort, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import json, mysql.connector
from sqlalchemy.ext.declarative import api


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=True)

db.create_all()

note_post_args = reqparse.RequestParser()
note_post_args.add_argument('title', type=str, help='Title is required', required=True)
note_post_args.add_argument('description', type=str, required=False)
note_post_args.add_argument('date', type=str, required=False)

note_put_args = reqparse.RequestParser()
note_put_args.add_argument('title', type=str, help='Title is required', required=True)
note_put_args.add_argument('description', type=str, required=False)
note_put_args.add_argument('date', type=str, required=False)

resource_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'date':fields.String
}

class NoteList(Resource):
    def get(self):
        titles = Note.query.all()
        database = {}
        for title in titles:
            database[title.id] = {"title":title.title, "description":title.description, "date":title.date}
        return database

class Note(Resource):
    @marshal_with(resource_fields)
    def post(self, id):
        args = note_post_args.parse_args()
        title = Note.query.filter_by(id=id).first()
        if title:
            abort(409, message="Note id taken.")

        result = Note(id=id, title=args['title'], description=args['description'], date=args['date'])
        db.session.add(result)
        db.session.commit()
        return result, 201

api.add_resource(Note,'/notes/<int:id>')
api.add_resource(NoteList, '/notes')


if __name__ == "__main__":
    app.run(debug=True)