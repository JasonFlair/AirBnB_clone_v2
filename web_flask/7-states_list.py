#!/usr/bin/python3
"""a  script that starts a Flask web application which listens on 0.0.0.0"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def calls_close():
    storage.close()

@app.route('/states_list', strict_slashes=False)
def list_of_states():
    """ returns a state list """
    states = storage.all("State")
    return render_template('7-state_lists.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)