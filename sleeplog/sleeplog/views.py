from pyramid.response import Response
from pyramid.view import view_config


class SleepLogViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(request):
        return Response('Placeholder')
