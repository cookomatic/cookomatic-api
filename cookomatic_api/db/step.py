"""Contains a database model for a Step."""

import flask
from google.appengine.ext import ndb

from cookomatic_api.util import db

db_step = flask.Blueprint('db_step', __name__)


@db_step.route('/v1/step/<int:step_id>')
def get_step(step_id):
    """API method to get a step by ID."""
    step = db.generic_get(Step, step_id)
    return flask.jsonify(step)


@db_step.route('/v1/step', methods=['POST'])
def save_step():
    """API method to save a step."""
    return db.generic_save(Step, 'step')


class Step(ndb.Model):
    """Models a unit of instruction for cooking a Dish."""
    name = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    estimated_time = ndb.IntegerProperty(required=True)
    snooze_time = ndb.IntegerProperty(default=0)
    ingredients = ndb.StringProperty(repeated=True)
