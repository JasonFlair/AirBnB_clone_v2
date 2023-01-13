#!/usr/bin/python3
"""
A simple script that starts a Flask web application which listens on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text
"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """simply returns Hello HBNB"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """simply returns HBNB"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text= "is cool"):
    """returns C followed by given text, else followed by is cool"""
    spaced_text = text.replace("_", " ")
    return 'C {}'.format(spaced_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
