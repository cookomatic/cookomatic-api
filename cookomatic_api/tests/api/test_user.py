import unittest

from google.appengine.ext import ndb
from google.appengine.ext import testbed

from cookomatic_api.db.user import User


class TestUser(unittest.TestCase):
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

    def tearDown(self):
        self.testbed.deactivate()

    def test_user(self):
        User(email='abc123@example.com').put()
        user = User.get_by_email('abc123@example.com')
        self.assertTrue(user)

    def test_user_doesnt_exist(self):
        User.get_by_email('abc123@example.com')
        self.assertRaises(RuntimeError)


if __name__ == '__main__':
    unittest.main()
