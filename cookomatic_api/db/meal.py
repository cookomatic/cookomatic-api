"""Contains a database model for a Meal."""

import flask
from google.appengine.ext import ndb

from cookomatic_api import util
from cookomatic_api.db.dish import Dish
from cookomatic_api.scheduling import Schedule

db_meal = flask.Blueprint('db_meal', __name__)


@db_meal.route('/v1/meal/<int:meal_id>')
@util.api.authenticate
def get_meal(user, meal_id):
    """API method to get a meal by ID."""
    obj = Meal.get_by_id(meal_id)
    return flask.jsonify(obj.serialize())


@db_meal.route('/v1/meal', methods=['POST'])
@util.api.authenticate
def save_meal(user):
    """API method to save a meal."""
    data = flask.request.get_json()

    # Convert IDs to Keys
    data = util.db.id_to_key(data, props={'dishes': Dish})

    return util.api.generic_save(Meal, data=data, extra_calls=['gen_schedule'])


class Meal(ndb.Model):
    """Models a collection of dishes that forms a meal."""
    name = ndb.StringProperty(required=True)

    # List of Dish keys
    dishes = ndb.KeyProperty(repeated=True)

    # Schedule generated for this meal
    schedule = ndb.JsonProperty()

    @property
    def ingredients(self):
        """Return a sorted list of ingredients used in this schedule."""
        ingredients = []
        for dish_key in self.dishes:
            dish = dish_key.get()
            for ingredient in dish.ingredients:
                ingredients.append(ingredient.pretty)

        return sorted(set(ingredients))

    def gen_schedule(self):
        """Generate a schedule for this meal."""
        if self.dishes:
            sched = Schedule(self)
            self.schedule = sched.serialize()

    def serialize(self):
        """Serializes entity."""
        data = self.to_dict()
        data['id'] = self.key.id()

        # Serialize properties
        data = util.db.key_to_id(data, {'dishes': None})

        return data
