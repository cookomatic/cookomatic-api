"""Contains a database model for a Meal."""

import flask
from google.appengine.ext import ndb

from cookomatic_api.util import db

db_meal = flask.Blueprint('db_meal', __name__)


@db_meal.route('/v1/meal/<int:meal_id>')
def get_meal(meal_id):
    """API method to get a meal by ID."""
    meal = db.generic_get(Meal, meal_id)
    return flask.jsonify(meal)


@db_meal.route('/v1/meal', methods=['POST'])
def save_meal():
    """API method to save a meal."""
    return db.generic_save(Meal, 'meal')


class Meal(ndb.Model):
    """Models a collection of dishes that forms a meal."""
    name = ndb.StringProperty(required=True)

    # List of Dish keys
    dishes = ndb.KeyProperty(repeated=True)
