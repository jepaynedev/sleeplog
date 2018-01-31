from pyramid.security import Allow, Deny, Authenticated, Everyone


class Root(object):
    __acl__ = [
        (Allow, Authenticated, 'view'),
        (Deny, Everyone, 'view'),
    ]

    def __init__(self, request):
        pass
