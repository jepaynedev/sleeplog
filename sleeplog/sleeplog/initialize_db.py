import argparse
import sys

from sqlalchemy import engine_from_config

from pyramid.paster import get_appsettings, setup_logging
from .models import DBSession, Base


def main(argv=sys.argv):
    parser = argparse.ArgumentParser(
        description='Initializes the SleepLog database'
    )
    parser.add_argument('config_uri', type=str, help='Path to Pyramid config file.')
    args = parser.parse_args(sys.argv[1:])
    setup_logging(args.config_uri)
    settings = get_appsettings(args.config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
