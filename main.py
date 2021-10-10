from flask import Flask, jsonify, request, make_response
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import dataset
from sqlalchemy.ext.declarative import api


app = Flask(__name__)

db = dataset.connect('sqlite:///data.db')

table = db['notes']

def fetch_db(note_id):
    return table.find_one(id=note_id)

def fetch_db_all():
    notes = []
    for note in table:
        notes.append(note)
    return notes

@app.route('/populate', methods=['GET'])
def populate():
    table.insert({
        "id": "1",
        "title": "A Song of Ice and Fire",
        "description": "A good old book",
        "date": "Out 9 2021"
    })
    table.insert({
        "id": "2",
        "title": "Food",
        "description": "Pizza",
        "date": "Out 8 2021"
    })
    return make_response(jsonify(fetch_db_all()),200)

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    if request.method == "GET":
        return make_response(jsonify(fetch_db_all()),200)
    elif request.method == "POST":
        content = request.json
        note_id = content['id']
        table.insert(content)
        return make_response(jsonify(fetch_db(note_id)), 201)

@app.route('/notes/<note_id>', methods=['GET', 'PUT', 'DELETE'])    
def each_note(note_id):
    if request.method == "GET":
        note_obj = fetch_db(note_id)
        if note_obj:
            return make_response(jsonify(note_obj),200)
        else:
            return make_response(jsonify(note_obj),404)

    elif request.method == "PUT":
        content = request.json
        table.update(content, ['id'])
        note_obj = fetch_db(note_id)
        return make_response(jsonify(note_obj), 200)

    elif request.method == "DELETE":
        table.delete(id=note_id)
        return make_response(jsonify({}),204)


if __name__ == "__main__":
    app.run(debug=True)