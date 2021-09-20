from typing import get_args
from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def main():
    retorno = None

    nota = request.args.get('Digite algo')

    retorno = get_args(nota)

    return render_template('index.html', nota=nota, retorno=retorno)

if __name__ == "__main__":
    app.run(debug=True)