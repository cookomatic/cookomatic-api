import json
import unittest

from flask_testing import TestCase
from google.appengine.ext import ndb
from google.appengine.ext import testbed

from cookomatic_api import api
from cookomatic_api.db.meal import Meal


class TestMeal(TestCase):
    def setUp(self):
        # Set up Cloud Datastore testbed
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        ndb.get_context().clear_cache()

    def tearDown(self):
        self.testbed.deactivate()

    def create_app(self):
        app = api.app
        return app

    def test_get_meal(self):
        meal_id = Meal(name='Meal 1').put().id()
        expected = {'name': 'Meal 1', 'dishes': []}

        response = self.client.get('/v1/meal/%s' % meal_id, content_type='application/json')

        self.assertEqual(expected, response.json)

    def test_save_meal(self):
        data = json.dumps({'name': 'Meal 1'})

        self.client.post('/v1/meal', data=data, content_type='application/json')

        self.assertEqual(1, len(Meal.query().fetch(2)))


if __name__ == '__main__':
    unittest.main()
