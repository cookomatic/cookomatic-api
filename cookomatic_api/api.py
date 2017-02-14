"""Handles the HTTP routing."""

import json

import flask
from flask import request

from cookomatic_api.db.dish import Dish

app = flask.Flask(__name__)


@app.route('/v1/dish/<int:dish_id>')
def get_dish(dish_id):
    """API method to get a dish by ID."""
    dish = Dish.get_by_id(dish_id)
    return json.dumps({'dish.name': dish.name})


@app.route('/v1/dish', methods=['POST'])
def save_dish():
    """API method to save a dish."""
    new_dish = Dish(name=request.form["name"])
    new_dish_key = new_dish.put()
    return json.dumps({'dish_id': new_dish_key.id()})


@app.errorhandler(404)
def page_not_found(_):
    """Return a 404 error."""
    return '', 404
