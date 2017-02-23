"""Generates meal schedule."""

import random

import flask

from cookomatic_api.db.step import Step

api_schedule = flask.Blueprint('api_schedule', __name__)


def generate_mock_schedule(meal_id):
    """Generates a mock schedule until we build out the actual algorithm."""
    return {
        'meal_id': meal_id,
        'steps': [
            Step(name='Step 1',
                 description='This is Step 1.',
                 estimated_time=random.randrange(1, 10),
                 dish_id=random.randrange(0, 999999),
                 ingredients=[
                     'Cheese',
                     'Bacon'
                 ]).to_dict(),
            Step(name='Step 2',
                 description='This is Step 2.',
                 estimated_time=random.randrange(1, 10),
                 dish_id=random.randrange(0, 999999),
                 ingredients=[
                     'Alfredo Sauce',
                     'Pasta'
                 ]).to_dict(),
            Step(name='Step 3',
                 description='This is Step 3.',
                 estimated_time=random.randrange(1, 10),
                 dish_id=random.randrange(0, 999999),
                 ingredients=[
                     'Chicken',
                     'Marinade'
                 ]).to_dict(),
        ]
    }


@api_schedule.route('/v1/schedule/<int:meal_id>')
def get_schedule(meal_id):
    """API method to get meal schedule."""
    schedule = generate_mock_schedule(meal_id)
    return flask.jsonify(schedule)
