import unittest

from pyramid import testing


class SleepLogViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import SleepLogViews

        request = testing.DummyRequest()
        inst = SleepLogViews(request)
        response = inst.home()
        self.assertEqual(b'Placeholder', response.body)
