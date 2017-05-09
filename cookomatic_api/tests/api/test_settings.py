import unittest

from google.appengine.ext import ndb
from google.appengine.ext import testbed

from cookomatic_api.db.settings import Settings


class TestSettings(unittest.TestCase):
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

        Settings(google_client_id='abc123').put()

    def tearDown(self):
        self.testbed.deactivate()

    def test_settings(self):
        settings = Settings.get()
        self.assertTrue(settings)


if __name__ == '__main__':
    unittest.main()
