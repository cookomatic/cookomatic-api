import unittest

from flask_testing import TestCase

from cookomatic_api import api


class TestHttpHandler(TestCase):
    def create_app(self):
        app = api.app
        return app

    def test_404(self):
        response = self.client.get('/asdf')

        self.assert404(response)


if __name__ == '__main__':
    unittest.main()
