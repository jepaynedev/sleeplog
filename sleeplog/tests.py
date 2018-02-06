import transaction
import unittest
import unittest.mock as mock

from pyramid import testing

from .models import User


class SleepLogViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_default(self):
        from .views.default import SleepLogViews

        request = testing.DummyRequest()
        request.user = User(
            sub='105578945702061677132',
            email='jepayne1138@gmail.com',
            verified=1,
            name='James Payne',
            given='James',
            family='James',
            locale='en',
            picture='https://lh3.googleusercontent.com/-cc2Wq0RJZ7g/AAAAAAAAAAI/AAAAAAAAAFc/mx6nAXHHaOc/s96-c/photo.jpg',
        )
        inst = SleepLogViews(request)
        response = inst.default()
        # Not ideal, but I want to quickly have a way to keep the id secret
        self.assertTrue(response['client_id'].endswith('.apps.googleusercontent.com'))
        self.assertEqual(response['given'], 'James')


class SleepLogFunctionalTests(unittest.TestCase):
    def setUp(self):
        from pyramid.paster import get_app
        app = get_app('production.ini')
        from webtest import TestApp
        self.testapp = TestApp(app)

    def tearDown(self):
        transaction.abort()

    @mock.patch('sleeplog.views.default.verify_google_token', return_value='105578945702061677132', autospec=True)
    def _login(self, *args):
        redirect_res = self.testapp.post(
            '/login',
            params={'form.submitted': 'Log In', 'token': 'dummy_token'},
            status=302,
        )
        redirect_res.follow(status=200)

    @mock.patch('sleeplog.views.default.verify_google_token', return_value='105578945702061677132', autospec=True)
    def test_login(self, mock_verify):
        self.testapp.post(
            '/login',
            params={'form.submitted': 'Log In', 'token': 'dummy_token'},
            status=302,
        )
        self.assertTrue(mock_verify.called)

    def test_default(self):
        self._login()
        res = self.testapp.get('/', status=200)
        self.assertIn(b'Welcome, James!', res.body)
        self.assertIn(b'.apps.googleusercontent.com', res.body)
