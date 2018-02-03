import unittest

from pyramid import testing


class SleepLogViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_default(self):
        from .views.default import SleepLogViews

        request = testing.DummyRequest()
        inst = SleepLogViews(request)
        response = inst.default()
        # Not ideal, but I want to quickly have a way to keep the id secret
        self.assertTrue(response['client_id'].endswith('.apps.googleusercontent.com'))


class SleepLogFunctionalTests(unittest.TestCase):
    def setUp(self):
        from pyramid.paster import get_app
        app = get_app('development.ini')
        from webtest import TestApp
        self.testapp = TestApp(app)

    def tearDown(self):
        pass

    def test_default(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'.apps.googleusercontent.com', res.body)
