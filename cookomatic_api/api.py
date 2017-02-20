"""Handles the HTTP routing."""

from flask import Flask
from flask import jsonify
from flask import request

from cookomatic_api.db.dish import Dish

app = Flask(__name__)


@app.route('/v1/dish/<int:dish_id>')
def get_dish(dish_id):
    """API method to get a dish by ID."""
    dish = Dish.get_by_id(dish_id)
    return jsonify({'dish.name': dish.name})


@app.route('/v1/dish', methods=['POST'])
def save_dish():
    """API method to save a dish."""
    data = request.get_json()
    new_dish = Dish(name=data['name'])
    new_dish_key = new_dish.put()
    return jsonify({'dish_id': new_dish_key.id()})


@app.errorhandler(404)
def page_not_found(_):
    """Return a 404 error."""
    return '', 404
