from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

from .models.config import authtkt_secret, session_secret


def main(global_config, **settings):
    session_factory = SignedCookieSessionFactory(session_secret)
    config = Configurator(
        settings=settings,
        root_factory='.action.security.Root',
        session_factory=session_factory,
    )
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.models.user')
    config.include('.routes')

    # Security policies
    authn_policy = AuthTktAuthenticationPolicy(
        authtkt_secret,
        hashalg='sha512',
    )
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.set_default_permission('view')

    config.scan()
    return config.make_wsgi_app()
