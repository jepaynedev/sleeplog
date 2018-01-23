import logging
log = logging.getLogger(__name__)

from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('home', '/')
    config.scan('.views')
    return config.make_wsgi_app()