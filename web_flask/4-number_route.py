#!/usr/bin/python3
"""
Flask web task 1
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """returns c text"""
    text = text.replace("_", " ")
    return 'C ' + text


@app.route('/python/<text>', strict_slashes=False)
def pytext(text):
    """returns py text"""
    text = text.replace("_", " ")
    return 'Python  ' + text


@app.route('/number/<n>', strict_slashes=False)
def isnumb(number):
    """returns number int"""
    number = int(number)
    return number + ' is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
