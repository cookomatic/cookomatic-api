import json
import unittest

from flask_testing import TestCase
from google.appengine.ext import ndb
from google.appengine.ext import testbed

from cookomatic_api import api
from cookomatic_api.db.dish import Dish
from cookomatic_api.db.meal import Meal
from cookomatic_api.db.step import Step

EXPECTED = """
    [
      {
        "description": null, 
        "estimated_time": 10.0, 
        "ingredients": [], 
        "is_user_intensive": true, 
        "name": "Dish 2, Step 1", 
        "snooze_time": 0.0, 
        "start_time": 0.0
      }, 
      {
        "description": null, 
        "estimated_time": 10.0, 
        "ingredients": [], 
        "is_user_intensive": true, 
        "name": "Dish 1, Step 1", 
        "snooze_time": 0.0, 
        "start_time": 10.0
      }, 
      {
        "description": null, 
        "estimated_time": 10.0, 
        "ingredients": [], 
        "is_user_intensive": false, 
        "name": "Dish 2, Step 2", 
        "snooze_time": 0.0, 
        "start_time": 20.0
      }, 
      {
        "description": null, 
        "estimated_time": 10.0, 
        "ingredients": [], 
        "is_user_intensive": false, 
        "name": "Dish 1, Step 2", 
        "snooze_time": 0.0, 
        "start_time": 20.5
      }, 
      {
        "description": null, 
        "estimated_time": 10.0, 
        "ingredients": [], 
        "is_user_intensive": true, 
        "name": "Dish 2, Step 3", 
        "snooze_time": 0.0, 
        "start_time": 21.0
      }, 
      {
        "description": null, 
        "estimated_time": 10.0, 
        "ingredients": [], 
        "is_user_intensive": true, 
        "name": "Dish 1, Step 3", 
        "snooze_time": 0.0, 
        "start_time": 31.0
      }, 
      {
        "description": null, 
        "estimated_time": 10.0, 
        "ingredients": [], 
        "is_user_intensive": true, 
        "name": "Dish 2, Step 4", 
        "snooze_time": 0.0, 
        "start_time": 41.0
      }, 
      {
        "description": null, 
        "estimated_time": 10.0, 
        "ingredients": [], 
        "is_user_intensive": true, 
        "name": "Dish 1, Step 4", 
        "snooze_time": 0.0, 
        "start_time": 51.0
      }, 
      {
        "description": null, 
        "estimated_time": 10.0, 
        "ingredients": [], 
        "is_user_intensive": false, 
        "name": "Dish 2, Step 5", 
        "snooze_time": 0.0, 
        "start_time": 61.0
      }, 
      {
        "description": null, 
        "estimated_time": 10.0, 
        "ingredients": [], 
        "is_user_intensive": false, 
        "name": "Dish 1, Step 5", 
        "snooze_time": 0.0, 
        "start_time": 61.5
      }
    ]
"""


class TestSchedule(TestCase):
    def setUp(self):
        # Set up Cloud Datastore testbed
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_search_stub()
        self.testbed.init_memcache_stub()
        ndb.get_context().clear_cache()

    @staticmethod
    def create_meal():
        meal = Meal(name='Meal 1')

        dish1 = Dish(
            name="Dish 1",
            tmp_steps=[
                Step(
                    name='Dish 1, Step 1',
                    estimated_time=10
                ),
                Step(
                    name='Dish 1, Step 2',
                    estimated_time=10,
                    is_user_intensive=False
                ),
                Step(
                    name='Dish 1, Step 3',
                    estimated_time=10,
                    tmp_depends_on=[1]
                ),
                Step(
                    name='Dish 1, Step 4',
                    estimated_time=10,
                    tmp_depends_on=[2]
                ),
                Step(
                    name='Dish 1, Step 5',
                    estimated_time=10,
                    is_user_intensive=False
                ),
            ]
        )
        dish1.parse_step_deps()
        meal.dishes.append(dish1.put())

        dish2 = Dish(
            name="Dish 2",
            tmp_steps=[
                Step(
                    name='Dish 2, Step 1',
                    estimated_time=10
                ),
                Step(
                    name='Dish 2, Step 2',
                    estimated_time=10,
                    is_user_intensive=False
                ),
                Step(
                    name='Dish 2, Step 3',
                    estimated_time=10,
                    tmp_depends_on=[1]
                ),
                Step(
                    name='Dish 2, Step 4',
                    estimated_time=10,
                    tmp_depends_on=[2]
                ),
                Step(
                    name='Dish 2, Step 5',
                    estimated_time=10,
                    is_user_intensive=False
                ),
            ]
        )
        dish2.parse_step_deps()
        meal.dishes.append(dish2.put())

        meal.gen_schedule()

        return meal.put().id()

    def tearDown(self):
        self.testbed.deactivate()

    def create_app(self):
        app = api.app
        return app

    def test_get_schedule(self):
        meal_id = self.create_meal()

        response = self.client.get('/v1/meal/%s' % meal_id, content_type='application/json')
        schedule = response.json['schedule']['steps']

        # It isn't necessary to compare IDs, etc. (since they will be different every time),
        # so remove them from output
        for step in schedule:
            step.pop('id')
            step.pop('depends_on')
            if 'tmp_depends_on' in step:
                step.pop('tmp_depends_on')

        self.assertEqual(json.loads(EXPECTED), schedule)


if __name__ == '__main__':
    unittest.main()
