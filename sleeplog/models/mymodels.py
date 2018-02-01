from sqlalchemy import Column, Integer, Numeric, Text, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .meta import Base


class Sleeper(Base):
    __tablename__ = 'sleeper'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    user_sub = Column(Text, ForeignKey('user.sub'))
    user = relationship('User', backref='sleeper_entries')
    time_asleep = Column(DateTime, nullable=False)
    time_awake = Column(DateTime, nullable=False)
    sleep_hours = Column(Numeric, nullable=False)
    tiredness = Column(Integer, nullable=False)
    headache = Column(Integer, nullable=False)  # Boolean
    est_wakes = Column(Integer, nullable=False)
    dream = Column(Text, nullable=False)
    comments = Column(Text, nullable=True)


class Observer(Base):
    __tablename__ = 'observer'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    user_sub = Column(Text, ForeignKey('user.sub'))
    user = relationship('User', backref='observer_entries')
    snore_type = Column(Text, nullable=False)
    wakes = Column(Integer, nullable=False)
    roll_over_help = Column(Integer, nullable=True)  # Boolean
    est_apnea = Column(Integer, nullable=True)
    couch_sleep = Column(Integer, nullable=False)  # Boolean
    comments = Column(Text, nullable=True)


class User(Base):
    __tablename__ = 'user'
    sub = Column(Text, primary_key=True)
    email = Column(Text, nullable=False)
    verified = Column(Integer, nullable=False)  # Boolean
    name = Column(Text, nullable=False)
    given = Column(Text, nullable=False)
    family = Column(Text, nullable=False)
    locale = Column(Text, nullable=False)
    picture = Column(Text, nullable=False)
