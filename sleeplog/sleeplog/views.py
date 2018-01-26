from pyramid.view import view_config, view_defaults

from .google_oauth_config import credentials


@view_defaults(renderer='home.jinja2')
class SleepLogViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(request):
        return {
            'client_id': credentials['web']['client_id'],
        }
