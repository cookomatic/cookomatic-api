import json
import unittest

from flask_testing import TestCase
from google.appengine.ext import ndb
from google.appengine.ext import testbed

from cookomatic_api import api
from cookomatic_api.db.step import Step

STEP_PARAMS = {
    'name': 'Step 1',
    'description': 'This is Step 1',
    'estimated_time': 5,
    'dish_id': 12345,
    'ingredients': ['Ingredient 1', 'Ingredient 2']
}


class TestStep(TestCase):
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

    def test_get_step(self):
        step_id = Step(**STEP_PARAMS).put().id()
        expected = {'snooze_time': 0}
        expected.update(STEP_PARAMS)

        response = self.client.get('/v1/step/%s' % step_id, content_type='application/json')

        self.assertEqual(expected, response.json)

    def test_save_step(self):
        data = json.dumps(STEP_PARAMS)

        self.client.post('/v1/step', data=data, content_type='application/json')

        self.assertEqual(1, len(Step.query().fetch(2)))


if __name__ == '__main__':
    unittest.main()
