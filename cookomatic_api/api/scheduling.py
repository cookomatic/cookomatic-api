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
            Step(name='Marinate Chicken',
                 description='Place chicken and seasonings into a gallon sized bag.',
                 estimated_time=1,
                 dish_id=random.randrange(0, 999999),
                 ingredients=[
                     'Chicken',
                     'Seasonings'
                 ]).to_dict(),
            Step(name='Preheat Oven',
                 description='Preheat Oven to 400 degrees',
                 estimated_time=1,
                 dish_id=random.randrange(0, 999999)).to_dict(),
            Step(name='Heat Nonstick Skillet',
                 description='Place a large nonstick skillet over medium high heat and wait until warm.',
                 estimated_time=1,
                 dish_id=random.randrange(0, 999999)).to_dict(),
            Step(name='Season Carrots',
                 description='Add the carrots to a bowl and toss with remaining seasonings',
                 estimated_time=1,
                 dish_id=random.randrange(0, 999999),
                 ingredients=[
                     'Carrots',
                     'Seasonings'
                 ]).to_dict(),
            Step(name='Add Chicken to Skillet',
                 description='Add chicken to skillet and cook over medium heat for 30 seconds.',
                 estimated_time=1,
                 dish_id=random.randrange(0, 999999),
                 ingredients=[
                     'Chicken'
                 ]).to_dict(),
             Step(name='Flip Chicken',
                 description='Flip the chicken and cook for an additional 30 seconds',
                 estimated_time=1,
                 dish_id=random.randrange(0, 999999),
                 ingredients=[
                     'Chicken'
                 ]).to_dict(),
             Step(name='Remove Chicken From Skillet',
                 description='Remove browned chicken from the pan .',
                 estimated_time=1,
                 dish_id=random.randrange(0, 999999),
                 ingredients=[
                     'Chicken'
                 ]).to_dict(),
            Step(name='Add Pineapple and Rice',
                 description='Add pineapple and rice to skillet, cover and reduce to medium low, and cook for 45 seconds.',
                 estimated_time=1,
                 dish_id=random.randrange(0, 999999),
                 ingredients=[
                     'Pineapple',
                     'Rice'
                 ]).to_dict(),
            Step(name='Bake Carrots',
                 description='Place the carrots on a baking tray and put in oven. Cook for 1 minute.',
                 estimated_time=1,
                 dish_id=random.randrange(0, 999999),
                 ingredients=[
                     'Carrots'
                 ]).to_dict(),
            Step(name='Add Chicken to Skillet',
                 description='Stir rice and nestle chicken on top and cook for an additional minute.',
                 estimated_time=1,
                 dish_id=random.randrange(0, 999999),
                 ingredients=[
                     'Chicken',
                     'Rice'
                 ]).to_dict(),
        ]
    }


@api_schedule.route('/v1/schedule/<int:meal_id>')
def get_schedule(meal_id):
    """API method to get meal schedule."""
    schedule = generate_mock_schedule(meal_id)
    return flask.jsonify(schedule)
