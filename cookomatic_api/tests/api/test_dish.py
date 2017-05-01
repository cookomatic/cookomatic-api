import json
import unittest

from flask_testing import TestCase
from google.appengine.ext import ndb
from google.appengine.ext import testbed

from cookomatic_api import api
from cookomatic_api.db.dish import Dish
from cookomatic_api.db.ingredient import Ingredient
from cookomatic_api.db.step import Step


class TestDish(TestCase):
    def setUp(self):
        # Set up Cloud Datastore testbed
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_search_stub()
        self.testbed.init_blobstore_stub()
        self.testbed.init_images_stub()
        self.testbed.init_memcache_stub()
        ndb.get_context().clear_cache()

        self.sample_dish = {
            'name': 'Dish 1',
            'img_filename': 'img.jpg',
            'ingredients': [
                Ingredient(name='tomatoes').serialize()
            ],
            'tags': ['indian', 'side dish'],
            'tools': ['strainer', 'starfish'],
            'prep_list': ['wash vegetables'],
            'steps': [
                Step(name='step 1',
                     description='baste',
                     estimated_time=5).put()
            ],
            'total_time': 35,
            'serving_size': 6
        }

    def tearDown(self):
        self.testbed.deactivate()

    def create_app(self):
        app = api.app
        app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
        return app

    def test_get_dish(self):
        dish = Dish(**self.sample_dish)
        dish.generate_img_url()
        dish_id = dish.put().id()
        expected = self.sample_dish
        expected['steps'] = [key.get().serialize() for key in expected['steps']]
        expected['estimated_time'] = 5
        expected['id'] = 2
        expected['owner'] = None
        expected['ingredients'] = ['tomatoes']

        response = self.client.get('/v1/dish/%s' % dish_id, content_type='application/json')
        r_json = response.json

        # Check img URLs and delete them from comparison
        self.assertEqual('/_ah/img/', r_json['img'][:9])
        self.assertEqual('/_ah/img/', r_json['img_thumb'][:9])
        r_json.pop('img')
        r_json.pop('img_thumb')

        self.assertEqual(expected, r_json)

    def test_save_dish(self):
        self.sample_dish['steps'] = [key.id() for key in self.sample_dish['steps']]
        json_data = json.dumps(self.sample_dish)

        self.client.post('/v1/dish', data=json_data, content_type='application/json')

        self.assertEqual(1, len(Dish.query().fetch(2)))


if __name__ == '__main__':
    unittest.main()
