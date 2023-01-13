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
    """simply returns hello hbnb"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """simply returns hbnb"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """returns C followed by specified text"""
    spaced_text = text.replace("_", " ")
    return 'C %s' % escape(spaced_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
