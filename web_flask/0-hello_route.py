#!/usr/bin/python3
"""a simple script that starts a Flask web application which listens on 0.0.0.0"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """ simply returns hello hbnb """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
