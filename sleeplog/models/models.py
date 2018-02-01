from sqlalchemy import Column, Integer#, Numeric, Text, Date, DateTime, Boolean, ForeignKey
# from sqlalchemy.orm import relationship

from .meta import Base


# class Sleeper(Base):
#     __tablename__ = 'sleeper'
#     id = Column('id', Integer, primary_key=True)
#     date = Column(Date, nullable=False)
#     # user_sub = Column(Text, ForeignKey('user.sub'))
#     # user = relationship('User', backref='sleeper_entries')
#     time_asleep = Column(DateTime, nullable=False)
#     time_awake = Column(DateTime, nullable=False)
#     sleep_hours = Column(Numeric, nullable=False)
#     tiredness = Column(Integer, nullable=False)
#     headache = Column(Boolean, nullable=False)
#     est_wakes = Column(Integer, nullable=False)
#     dream = Column(Text, nullable=False)
#     comments = Column(Text, nullable=True)


# class Observer(Base):
#     __tablename__ = 'observer'
#     id = Column('id', Integer, primary_key=True)
#     date = Column(Date, nullable=False)
#     # user_sub = Column(Text, ForeignKey('user.sub'))
#     # user = relationship('User', backref='observer_entries')
#     snore_type = Column(Text, nullable=False)
#     wakes = Column(Integer, nullable=False)
#     roll_over_help = Column(Boolean, nullable=True)
#     est_apnea = Column(Integer, nullable=True)
#     couch_sleep = Column(Boolean, nullable=False)
#     comments = Column(Text, nullable=True)


# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer)
    # sub = Column('sub', Text, primary_key=True)
    # email = Column(Text, nullable=False)
    # verified = Column(Boolean, nullable=False)
    # name = Column(Text, nullable=False)
    # given = Column(Text, nullable=False)
    # family = Column(Text, nullable=False)
    # locale = Column(Text, nullable=False)
    # picture = Column(Text, nullable=False)


from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)


Index('my_index', MyModel.name, unique=True, mysql_length=255)
