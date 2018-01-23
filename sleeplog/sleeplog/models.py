from pyramid.security import Allow, Everyone

from sqlalchemy import Column, Integer, Numeric, Text, Date, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(
    sessionmaker(extension=ZopeTransactionExtension())
)
Base = declarative_base()


class Sleeper(Base):
    __tablename__ = 'sleeper'
    date = Column(Date, primary_key=True)
    time_asleep = Column(DateTime, nullable=False)
    time_awake = Column(DateTime, nullable=False)
    sleep_hours = Column(Numeric, nullable=False)
    tiredness = Column(Integer, nullable=False)
    headache = Column(Boolean, nullable=False)
    est_wakes = Column(Integer, nullable=False)
    dream = Column(Text, nullable=False)
    comments = Column(Text, nullable=True)


class Observer(Base):
    __tablename__ = 'observer'
    date = Column(Date, primary_key=True)
    snore_type = Column(Text, nullable=False)
    wakes = Column(Integer, nullable=False)
    roll_over_help = Column(Boolean, nullable=True)
    est_apnea = Column(Integer, nullable=True)
    couch_sleep = Column(Boolean, nullable=False)
    comments = Column(Text, nullable=True)


class Root(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, 'group:editors', 'edit')]

    def __init__(self, request):
        pass
