from pyramid.security import unauthenticated_userid

from ..models import User


def get_user(request):
    userid = unauthenticated_userid(request)
    if userid is not None:
        # this should return None if the user doesn't exist
        # in the database
        print('getting user')
        return request.dbsession.query(User).filter(User.sub == userid)


def includeme(config):
    config.add_request_method(get_user, 'user', reify=True)
