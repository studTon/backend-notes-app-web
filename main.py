from typing import get_args
from flask import Flask, jsonify
from flask.globals import request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        nota = request.get_json()
        return jsonify({"nota":nota}), 201
    else:
        return jsonify({"about":"hello world"})

@app.route('/<text>', methods=['GET'])
def criar_nota(text):
    return jsonify({'Texto':text})

if __name__ == "__main__":
    app.run(debug=True)