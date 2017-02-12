import unittest

from cookomatic_api import api


class TestDish(unittest.TestCase):
    def setUp(self):
        self.app = api.app.test_client()

    def test_get_dish(self):
        response = api.get_dish(1)
        self.assertEqual(response, 'Dish id 1')

    def test_save_dish(self):
        data = {'name': 'pizza'}
        with api.app.test_request_context('/dish', method='POST', data=data):
            response = api.save_dish()
            self.assertEqual(response, 'pizza')


if __name__ == '__main__':
    unittest.main()
