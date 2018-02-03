from pyramid.security import unauthenticated_userid

from ..models import User


def get_user(request):
    userid = unauthenticated_userid(request)
    if userid is not None:
        # this should return None if the user doesn't exist
        # in the database

        # If I'm misunderstanding something, I may want to use scalar()
        # instead of one(), but I think the user should always be in the
        # database at this point
        return request.dbsession.query(User).filter(User.sub == userid).one()


def includeme(config):
    config.add_request_method(get_user, 'user', reify=True)
