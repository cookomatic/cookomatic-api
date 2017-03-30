"""Contains a database model for a Step."""

import flask
from google.appengine.ext import ndb

from cookomatic_api import util
from cookomatic_api.db.ingredient import Ingredient

db_step = flask.Blueprint('db_step', __name__)


@db_step.route('/v1/step/<int:step_id>')
def get_step(step_id):
    """API method to get a step by ID."""
    obj = Step.get_by_id(step_id)

    # Serialize all Ingredient objects
    obj.ingredients = [ingred.to_dict() for ingred in obj.ingredients]

    return flask.jsonify(obj.to_dict())


@db_step.route('/v1/step', methods=['POST'])
def save_step():
    """API method to save a step."""
    data = flask.request.get_json()

    # Deserialize all Ingredient objects
    ingredients = [Ingredient(**i) for i in data['ingredients']]
    data['ingredients'] = ingredients

    return util.db.generic_save(Step, 'step', data=data)


class Step(ndb.Expando):
    """Models a unit of instruction for cooking a Dish."""
    name = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)

    # Does this step require a user's attention for the entire duration?
    is_user_intensive = ndb.BooleanProperty(default=True)

    # How long this step should take the user to complete
    estimated_time = ndb.IntegerProperty(required=True)

    # Used only by scheduler. What point in time this step is ready to be completed.
    start_time = ndb.IntegerProperty()

    # Number of seconds the step be snoozed if the user isn't ready to complete it.
    snooze_time = ndb.IntegerProperty(default=0)

    # List of keys of other Ingredients required by this step
    ingredients = ndb.StructuredProperty(Ingredient, repeated=True)

    # List of keys of other Steps that this depends on. Dish.parse_step_deps creates this.
    depends_on = ndb.KeyProperty(repeated=True)
