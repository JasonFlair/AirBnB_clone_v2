#!/usr/bin/python3
"""a  script that starts a Flask web application which listens on 0.0.0.0"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state_list():
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)

@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """ returns a state list with cities, sorted by name """
    state = storage.get(State, id)
    return render_template('9-states.html', state=state)

@app.teardown_appcontext
def calls_close(exc):
    """closes the current SQLAlchemy session."""
    storage.close()
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)