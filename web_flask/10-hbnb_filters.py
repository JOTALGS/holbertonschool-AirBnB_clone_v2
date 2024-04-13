#!/usr/bin/python3
"""
sdmasdnsajkdnsakdjhsajkdhsajkdhsajk dbsajkdbhsajdbsadbsahdb c sdd asd asd  sad sad sad sa
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """Shutdown the current session."""
    storage.close()


@app.route('/hbnb_filters')
def filters():
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda x: x.name)
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states_sorted, amenities=amenities)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port='5000')