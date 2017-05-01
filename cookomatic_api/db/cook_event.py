"""Contains a database model for a Cook Event."""

from datetime import datetime

import flask
from google.appengine.ext import ndb

from cookomatic_api import util
from cookomatic_api.db.meal import Meal
from cookomatic_api.db.user import User

db_cook_event = flask.Blueprint('db_cook_event', __name__)


def transform(data):
    """Perform common transforms on data."""
    data['meal'] = ndb.Key(Meal, data['meal'])
    data['time'] = datetime.fromtimestamp(data['time'])

    return data


@db_cook_event.route('/v1/cook_event/meal_rating/<int:meal_id>')
@util.api.authenticate
def get_meal_rating(user, meal_id):
    """API method to get a cook event by ID."""
    meal_key = ndb.Key(Meal, meal_id)
    rating = CookEvent.get_meal_rating(meal_key)
    return flask.jsonify({'meal_id': meal_id, 'rating': rating})


@db_cook_event.route('/v1/cook_event/<int:cook_event_id>')
@util.api.authenticate
def get_cook_event(user, cook_event_id):
    """API method to get a cook event by ID."""
    obj = CookEvent.get_by_id(cook_event_id)
    return flask.jsonify(obj.serialize())


@db_cook_event.route('/v1/cook_event', methods=['POST'])
@util.api.authenticate
def save_cook_event(user):
    """API method to save a cook event."""
    data = flask.request.get_json()
    data = transform(data)
    data['user'] = user.key

    return util.api.generic_save(CookEvent, data=data)


@db_cook_event.route('/v1/cook_event', methods=['PUT'])
@util.api.authenticate
def update_cook_event(user):
    """API method to update a cook event."""
    data = flask.request.get_json()
    data = transform(data)

    # Get entity that we're going to update
    entity_id = data.pop('id')
    entity = CookEvent.get_by_id(entity_id)

    # Update entity and save
    for key, value in data.iteritems():
        setattr(entity, key, value)

    # Transform data
    entity.put()

    return flask.jsonify(entity.serialize())


class CookEvent(ndb.Expando):
    """Models the event of a meal being cooked."""
    # The User who cooked the meal
    user = ndb.KeyProperty(required=True)

    # The meal that this entity is created to describe
    meal = ndb.KeyProperty(required=True)

    # When the meal was begun
    time = ndb.DateTimeProperty(required=True)

    # The list of minutes that correspond to the steps in the meal.schedule
    time_taken = ndb.FloatProperty(repeated=True)

    # The rating given to the meal from 1-5
    rating = ndb.IntegerProperty()

    # The text that the user leaves as a review for the meal
    review_text = ndb.StringProperty()

    def serialize(self):
        """Serializes entity."""
        data = self.to_dict()
        data['id'] = self.key.id()

        data['user'] = data['user'].id()
        data['meal'] = data['meal'].id()
        data['time'] = int(data['time'].strftime("%s"))

        return data

    @classmethod
    def get_meal_rating(cls, meal_key):
        """Returns an average rating for a given Meal."""
        query = cls.query(cls.meal == meal_key)
        ratings = [ce.rating for ce in query]
        if not ratings:
            return 0

        raw_avg = sum(ratings) / float(len(ratings))
        return round(raw_avg, 1)
