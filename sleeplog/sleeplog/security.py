from pyramid.security import Allow, Deny, Authenticated, Everyone
from google.oauth2 import id_token
from google.auth.transport import requests

from .configuration import google_client_id


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
