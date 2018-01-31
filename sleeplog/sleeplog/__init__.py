import logging
log = logging.getLogger(__name__)

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession, Base
from .configuration import authtkt_secret


def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(
        settings=settings,
        root_factory='.security.Root'
    )
    config.include('pyramid_tm')
    config.include('pyramid_jinja2')

    # Security policies
    authn_policy = AuthTktAuthenticationPolicy(
        authtkt_secret,
        hashalg='sha512',
    )
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.scan('.views')
    return config.make_wsgi_app()
