from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DBSession = scoped_session(sessionmaker())
Base = declarative_base()

from User import User
from State import State
from Club import Club
from Course import Course
from Tee import Tee
from Hole import Hole
from Round import Round
from Score import Score

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    #Create and/or check if new tables need to be created.
    Base.metadata.create_all(engine)