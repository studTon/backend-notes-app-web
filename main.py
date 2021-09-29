from flask import Flask, jsonify, render_template
from flask.globals import request
from data import json_object


app = Flask(__name__)
@app.route('/anotacoes')
def delete():
    return delete
@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello():
    return 'hello world'
'''class nota():
    def __init__(self) -> None:
        pass;
        self.title = request.form['title']
        self.id = request.form['id']
        self.date = request.form['date']
        self.description = request.form['description']'''

@app.route('/get', methods=['GET'])
def criar_nota():
    return render_template('template.html')
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