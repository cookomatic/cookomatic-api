"""Contains a database model for a Step."""

import flask
from google.appengine.ext import ndb

from cookomatic_api.db import util

db_step = flask.Blueprint('db_step', __name__)


@db_step.route('/v1/step/<int:step_id>')
def get_step(step_id):
    """API method to get a step by ID."""
    return util.generic_get(Step, step_id)


@db_step.route('/v1/step', methods=['POST'])
def save_step():
    """API method to save a step."""
    data = flask.request.get_json()
    return util.generic_save(Step, 'step', data)


class Step(ndb.Model):
    """Models a unit of instruction for cooking a Dish."""
    name = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    estimated_time = ndb.IntegerProperty(required=True)
    snooze_time = ndb.IntegerProperty(default=0)

    # These elements should be of KeyProperty type once we implement schedule
    # dish_id = ndb.KeyProperty(required=True)
    dish_id = ndb.IntegerProperty(required=True)
    # ingredients = ndb.KeyProperty(repeated=True)
    ingredients = ndb.IntegerProperty(repeated=True)
