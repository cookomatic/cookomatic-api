import json
import unittest
from datetime import datetime

from flask_testing import TestCase
from google.appengine.ext import ndb
from google.appengine.ext import testbed

from cookomatic_api import api
from cookomatic_api.db.cook_event import CookEvent

COOK_EVENT_PARAMS = {
    'user': 'Sally-Anne',
    'time': datetime(2012, 6, 25),
    'time_taken': [120, 260, 10],
    'rating': 3,
    'review_text': 'Really easy to make!'
}


class TestCookEvent(TestCase):
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

    def test_get_cook_event(self):
        cook_event = CookEvent(**COOK_EVENT_PARAMS)
        cook_event_id = cook_event.put().id()

        response = self.client.get('/v1/cook_event/%s' % cook_event_id,
                                   content_type='application/json')
        r_json = response.json

        self.assertEqual(cook_event.serialize(), r_json)

    def test_save_cook_event(self):
        cook_event = CookEvent(**COOK_EVENT_PARAMS)
        json_data = json.dumps(cook_event.serialize())

        self.client.post('/v1/cook_event', data=json_data, content_type='application/json')

        self.assertEqual(1, len(CookEvent.query().fetch(2)))


if __name__ == '__main__':
    unittest.main()
