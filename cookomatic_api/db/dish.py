"""Contains a database model for a Dish."""

import flask
from google.appengine.ext import ndb

from cookomatic_api.db import util
from cookomatic_api.db.step import Step

db_dish = flask.Blueprint('db_dish', __name__)


@db_dish.route('/v1/dish/<int:dish_id>')
def get_dish(dish_id):
    """API method to get a dish by ID."""
    return util.generic_get(Dish, dish_id, convert_keys=['steps'])


@db_dish.route('/v1/dish', methods=['POST'])
def save_dish():
    """API method to save a dish."""
    return util.generic_save(Dish, 'dish', convert_keys={'steps': Step})


class Dish(ndb.Model):
    """Models a collection of steps that form a single dish."""
    name = ndb.StringProperty(required=True)
    tags = ndb.StringProperty(repeated=True)
    tools = ndb.StringProperty(repeated=True)
    ingredients = ndb.StringProperty(repeated=True)
    prep_list = ndb.StringProperty(repeated=True)
    steps = ndb.KeyProperty(repeated=True)
    total_time = ndb.IntegerProperty()
    serving_size = ndb.IntegerProperty()
