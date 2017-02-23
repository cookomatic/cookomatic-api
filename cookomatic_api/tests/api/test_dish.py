import json
import unittest

from flask_testing import TestCase
from google.appengine.ext import ndb
from google.appengine.ext import testbed

from cookomatic_api import api
from cookomatic_api.db.dish import Dish


class TestDish(TestCase):
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

    def test_get_dish(self):
        dish_id = Dish(name='Dish 1').put().id()
        expected = {'name': 'Dish 1', 'steps': []}

        response = self.client.get('/v1/dish/%s' % dish_id, content_type='application/json')

        self.assertEqual(expected, response.json)

    def test_save_dish(self):
        data = json.dumps({'name': 'Dish 1'})

        self.client.post('/v1/dish', data=data, content_type='application/json')

        self.assertEqual(1, len(Dish.query().fetch(2)))


if __name__ == '__main__':
    unittest.main()
