#!/usr/bin/python3
"""
sdmasdnsajkdnsakdjhsajkdhsajkdhsajk dbsajkdbhsajdbsadbsahdb c sdd asd asd  sad sad sad sa
"""
from flask import Flask, render_template
from models import storage
from models.state import State, City

app = Flask(__name__)

storage.reload()


@app.teardown_appcontext
def app_close(exception=None):
    """ Teardown method """
    storage.close()


@app.route('/cities_by_state')
def states():
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states_sorted)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port='5000')
