from pyramid.security import Allow, Deny, Authenticated, Everyone
from google.oauth2 import id_token
from google.auth.transport import requests
import transaction

from .configuration import google_client_id
from .models import DBSession, User


def verify_google_token(token):
    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            google_client_id
        )

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        # While we have the parsed info, before returning, make sure we have
        # a valid database entry for this user, else create a new one
        with transaction.manager:
            model = User(
                sub=idinfo['sub'],
                email=idinfo['email'],
                verified=idinfo['email_verified'],
                name=idinfo['name'],
                given=idinfo['given_name'],
                family=idinfo['family_name'],
                locale=idinfo['locale'],
                picture=idinfo['picture'],
            )
            DBSession.merge(model)

        return idinfo['sub']
    except ValueError:
        # Invalid token
        return None


class Root(object):
    __acl__ = [
        (Allow, Authenticated, 'view'),
        (Deny, Everyone, 'view'),
    ]

    def __init__(self, request):
        pass
