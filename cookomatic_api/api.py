"""Handles the HTTP routing."""

import flask
from flask import request

app = flask.Flask(__name__)

SUCCESS = ('', 200)


@app.route('/v1/dish/<int:dish_id>')
def get_dish(dish_id):
    """API method to get a dish by ID."""
    return 'Dish id %d' % dish_id


@app.route('/v1/dish', methods=['POST'])
def save_dish():
    """API method to save a dish."""
    return request.form["name"]


@app.errorhandler(404)
def page_not_found(error):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL. Error msg: %s' % error, 404
