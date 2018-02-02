from sqlalchemy import Column, Integer, Numeric, Text, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .meta import Base


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


class SleepLog(Base):
    __tablename__ = 'sleeplog'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    created_sub = Column(Text, ForeignKey('user.sub'))
    created_by = relationship('User', backref='created')
    created_time = Column(DateTime, nullable=False)


class SleepLogRoles(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)


class SleepLogParticipants(Base):
    __tablename__ = 'participants'
    id = Column(Integer, primary_key=True)
    user_sub = Column(Text, ForeignKey('user.sub'))
    user = relationship('User', backref='sleeplogs')
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship('SleepLogRoles', backref='participants')
    join_time = Column(DateTime, nullable=False)
    left_time = Column(DateTime, nullable=False)
    # Other settings here


class SleepLogInvitations(Base):
    __tablename__ = 'invites'
    id = Column(Integer, primary_key=True)
    user_sub = Column(Text, ForeignKey('user.sub'))
    user = relationship('User', backref='sent_invites')
    recipient = Column(Text, nullable=True)
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship('SleepLogRoles', backref='invites')


class SleeperEntry(Base):
    __tablename__ = 'sleeper'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    user_sub = Column(Text, ForeignKey('user.sub'))
    user = relationship('User', backref='sleeper')
    time_asleep = Column(DateTime, nullable=False)
    time_awake = Column(DateTime, nullable=False)
    sleep_hours = Column(Numeric, nullable=False)
    tiredness = Column(Integer, nullable=False)
    headache = Column(Integer, nullable=False)  # Boolean
    est_wakes = Column(Integer, nullable=False)
    dream = Column(Text, nullable=False)
    comments = Column(Text, nullable=True)


class ObserverEntry(Base):
    __tablename__ = 'observer'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    user_sub = Column(Text, ForeignKey('user.sub'))
    user = relationship('User', backref='observer')
    snore_type = Column(Text, nullable=False)
    wakes = Column(Integer, nullable=False)
    roll_over_help = Column(Integer, nullable=True)  # Boolean
    est_apnea = Column(Integer, nullable=True)
    couch_sleep = Column(Integer, nullable=False)  # Boolean
    comments = Column(Text, nullable=True)
