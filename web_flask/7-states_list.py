#!/usr/bin/python3
"""a  script that starts a Flask web application which listens on 0.0.0.0"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def list_of_states():
    """ returns a state list, sorted by name """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def calls_close(exc):
    """closes the current SQLAlchemy session."""
    storage.close()
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
