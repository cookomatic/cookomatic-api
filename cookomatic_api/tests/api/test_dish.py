import json
import unittest

from flask_testing import TestCase
from google.appengine.ext import ndb
from google.appengine.ext import testbed

from cookomatic_api import api
from cookomatic_api.db.dish import Dish
from cookomatic_api.db.step import Step


class TestDish(TestCase):
    def setUp(self):
        # Set up Cloud Datastore testbed
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        ndb.get_context().clear_cache()

        self.sample_dish = {
            u'name': u'Dish 1',
            u'tags': [u'indian', u'side dish'],
            u'tools': [u'strainer', u'starfish'],
            u'ingredients': [u'tomatoes', u'fish'],
            u'prep_list': [u'wash vegetables'],
            u'steps': [
                Step(name=u'step 1',
                     description=u'baste',
                     estimated_time=5,
                     dish_id=0,
                     ingredients=[0]).put()
            ],
            u'total_time': 35,
            u'serving_size': 6
        }

    def tearDown(self):
        self.testbed.deactivate()

    def create_app(self):
        app = api.app
        return app

    def test_get_dish(self):
        dish_id = Dish(**self.sample_dish).put().id()
        expected = self.sample_dish
        expected['steps'] = [key.id() for key in expected['steps']]

        response = self.client.get('/v1/dish/%s' % dish_id, content_type='application/json')

        self.assertEqual(expected, response.json)

    def test_save_dish(self):
        self.sample_dish['steps'] = [key.id() for key in self.sample_dish['steps']]
        json_data = json.dumps(self.sample_dish)

        self.client.post('/v1/dish', data=json_data, content_type='application/json')

        self.assertEqual(1, len(Dish.query().fetch(2)))


if __name__ == '__main__':
    unittest.main()