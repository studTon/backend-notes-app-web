from flask import Flask, app, Blueprint, render_template, request
from flask.helpers import flash

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1 align="center">Anotações</h1>'

def post():
    ##if request.method == 'Post':
        ##post = request.form.get('post')
        ##if len(post) < 1:
        ##    flash('Anotação muito pequena!', category='error')
        ##else:
        ##    new_post = post()
        ##    flash('Anotado!', category='success')
    return render_template("index.html")