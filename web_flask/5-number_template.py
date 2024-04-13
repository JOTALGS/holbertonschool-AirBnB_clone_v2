#!/usr/bin/python3
"""
Flask web task 5
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """returns Hello"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def ctext(text):
    """returns c text"""
    text = text.replace("_", " ")
    return 'C ' + text


@app.route('/python', defaults={'text': "is_cool"})
@app.route('/python/<text>')
def pytext(text='is cool'):
    """returns py text"""
    text = text.replace("_", " ")
    return 'Python  ' + text


@app.route('/number/<int:n>')
def isnumb(n):
    """returns number int"""
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def numbert(n):
    """return template"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port='5000')
