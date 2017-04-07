"""Contains a database model for a Cook Event."""

from datetime import datetime

import flask
from google.appengine.ext import ndb

from cookomatic_api import util

db_cook_event = flask.Blueprint('db_cook_event', __name__)


@db_cook_event.route('/v1/cook_event/<int:cook_event_id>')
def get_cook_event(cook_event_id):
    """API method to get a cook event by ID."""
    obj = CookEvent.get_by_id(cook_event_id)
    return flask.jsonify(obj.serialize())


@db_cook_event.route('/v1/cook_event', methods=['POST'])
def save_cook_event():
    """API method to save a cook event."""
    data = flask.request.get_json()
    data['time'] = datetime(**data['time'])
    return util.db.generic_save(CookEvent, 'cook_event')


class CookEvent(ndb.Expando):
    """Models the event of a meal being cooked."""

    # The User who cooked the meal
    user = ndb.StringProperty(required=True)

    # When the meal was begun
    time = ndb.DateTimeProperty(required=True)

    # The list of seconds that correspond to the steps in the meal.schedule
    time_taken = ndb.IntegerProperty(repeated=True)

    # The rating given to the meal from 1-5
    rating = ndb.IntegerProperty()

    # The text that the user leaves as a review for the meal
    review_text = ndb.StringProperty()

    def serialize(self):
        """Serializes entity."""
        data = self.to_dict()
        data['time'] = {'year': self.time.year, 'month': self.time.month, 'day': self.time.day}

        return data
