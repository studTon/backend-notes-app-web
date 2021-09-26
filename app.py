from typing import get_args
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({"about":"hello world"})

if __name__ == "__main__":
    app.run(debug=True)