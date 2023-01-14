#!/usr/bin/python3
"""
A simple script that starts a Flask web application which listens on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text
/python/(<text>): display “Python ”, followed by the value of the text variable
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer
"""
from flask import Flask, render_template
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

@app.route('/python',strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """returns Python followed by given text, else followed by is cool
       :param text: the text to be returned after Python"""
    spaced_text = text.replace("_", " ")
    return 'Python {}'.format(spaced_text)

@app.route('/number/<int:n>', strict_slashes=False)
def check_num(n):
    """checks if n is a number using the int converter"""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """rendering a html with n as the number"""
    return render_template('5-number.html', number=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """returns even or odd depending"""
    if (n % 2 == 0):
        even_odd = "even"
        return render_template('6-number_odd_or_even.html', number=n, even_odd=even_odd)
    else:
        even_odd = "odd"
        return render_template('6-number_odd_or_even.html', number=n, even_odd=even_odd)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
