from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, view_defaults, forbidden_view_config
from pyramid.security import remember, forget, NO_PERMISSION_REQUIRED

from ..models.config import google_client_id
from ..action.security import verify_google_token


@view_defaults(renderer='../templates/default.jinja2')
class SleepLogViews:

    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid

    @view_config(route_name='default')
    def default(self):
        user = self.request.user
        return dict(
            given=user.given,
            client_id=google_client_id,
        )

    @view_config(route_name='login', renderer='../templates/login.jinja2', permission=NO_PERMISSION_REQUIRED)
    @forbidden_view_config(renderer='../templates/login.jinja2')
    def login(self):
        request = self.request
        login_url = request.route_url('login')
        referrer = request.url
        if referrer == login_url:
            referrer = '/'  # never use login form itself as came_from
        came_from = request.params.get('came_from', referrer)
        user_id = ''
        if 'form.submitted' in request.params:
            token = request.params['token']
            user_id = verify_google_token(token, request)
            if user_id:
                headers = remember(request, user_id)
                return HTTPFound(
                    location=came_from,
                    headers=headers
                )
        return dict(
            url=request.application_url + '/login',
            came_from=came_from,
            token=user_id,
            client_id=google_client_id,
        )

    @view_config(route_name='logout')
    def logout(self):
        request = self.request
        headers = forget(request)
        url = request.route_url('default')
        return HTTPFound(
            location=url,
            headers=headers
        )
