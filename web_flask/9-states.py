from flask import Flask, render_template
from models import storage
from models.state import State, City

app = Flask(__name__)


@app.teardown_appcontext
def app_close(exception=None):
    """ Teardown method """
    storage.close()


@app.route('/states')
def states():
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=states_sorted)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return "<H1>Not found!</H1>"

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port='5000')
