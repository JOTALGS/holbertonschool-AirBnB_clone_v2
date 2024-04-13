from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def app_close(exception=None):
    """ Teardown method """
    storage.close()


@app.route('/states_list')
def states():
    states = storage.all(State).values()
    print(states)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port='5000')
