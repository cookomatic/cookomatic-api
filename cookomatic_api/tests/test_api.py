import unittest
import sys

from google.appengine.ext import ndb
from google.appengine.ext import testbed

from cookomatic_api import api
from cookomatic_api.db.dish import Dish

sys.path.insert(1, 'google-cloud-sdk/platform/google_appengine')
sys.path.insert(1, 'google-cloud-sdk/platform/google_appengine/lib/yaml/lib')


class TestDish(unittest.TestCase):
    def setUp(self):
        self.app = api.app.test_client()

        # Set up Cloud Datastore testbed
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        ndb.get_context().clear_cache()

    def tearDown(self):
        self.testbed.deactivate()

    def test_get_dish(self):
        dish_id = Dish(name='Pizza').put().id()
        expected = '{"dish.name": "Pizza"}'

        response = api.get_dish(dish_id)

        self.assertEqual(response, expected)

    def test_save_dish(self):
        data = {'name': 'pizza'}

        with api.app.test_request_context('/dish', method='POST', data=data):
            api.save_dish()

            self.assertEqual(1, len(Dish.query().fetch(2)))


if __name__ == '__main__':
    unittest.main()
