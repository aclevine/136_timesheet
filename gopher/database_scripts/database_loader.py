from csv import DictReader
from gzip import GzipFile
import os
import sys
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


localpath = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(localpath, os.pardir)))

from sqlalchemy import create_engine
from gopher import models
from gopher.models import *

DBSession = scoped_session(sessionmaker())
Base = declarative_base()

# engine = create_engine('postgresql://Colin:bombadil@localhost/gopher')
engine = create_engine('sqlite+pysqlite:///'+os.path.abspath(os.path.join(localpath, os.pardir)) + '/gopher.db')
models.init_model(engine)


def add_unique(record):
    try:
        DBSession.add(record)
        DBSession.commit()
    except (IntegrityError, InvalidRequestError):
        DBSession.rollback()

def append_item(child, attribute):
        if child not in attribute:
            attribute.append(child)

def insert_unique_relationship(name, id1, id2):
    try:
        DBSession.execute("insert into {} values ({},{})".format(name, id1, id2))
        DBSession.commit()
    except (IntegrityError, InvalidRequestError):
        DBSession.rollback()

if __name__ == '__main__':

    club_reader = DictReader(GzipFile('Golf Clubs-Table 1.csv.gz'), delimiter=',', quotechar='"')
    course_reader = DictReader(GzipFile('Golf Courses-Table 1.csv.gz'), delimiter= ',', quotechar= '"')
    scorecard_reader = DictReader(GzipFile('Scorecards-Table 1.csv.gz'), delimiter= ',', quotechar= '"')

    for row in club_reader:
        state = State(row["state_province_name"])

        add_unique(state)
        state = DBSession.query(State).filter(State.name== row["state_province_name"]).one()

        club = Club(row["facility_id"], row["facility_name"], row["address"], row["city_name"], state.id, row["website"], float(row["longitude"]), float(row["latitude"]), int(row["number_of_holes"]))
        
        add_unique(club)
        club= DBSession.query(Club).filter(Club.facility_id==row["facility_id"]).one()
        append_item(club, state.clubs)
        DBSession.commit()
      
    for row in course_reader:
        club = DBSession.query(Club).filter(Club.facility_id==row["facility_id"]).one()
        course = Course(row["course_id"], club.facility_id, row["course_name"], int(row["holes"]), row["par"], row["course_architect"], row["open_date"])
        
        add_unique(course)
        course = DBSession.query(Course).filter(Course.course_id== row["course_id"]).one()
        append_item(course, club.courses)
        DBSession.commit()

    for row in scorecard_reader:
        course = DBSession.query(Course).filter(Course.course_id == row["course_id"]).one()

        tee = Tee(row["tee_id"], course.course_id, row["tee_name"], row["tee_color"], int(row["course_par_for_tee"]), int(row["total_distance"]))
        add_unique(tee)
        tee = DBSession.query(Tee).filter(Tee.tee_id== row["tee_id"]).one()
        append_item(tee, course.tees)
        
        DBSession.commit()

        for i in range(1,19):
            if row["hole"+str(i)]!= "~":
                hole = Hole(i, tee.tee_id, int(row["hole"+str(i)+"_par"]), int(row["hole"+str(i)]))

                add_unique(hole)
                hole = DBSession.query(Hole).filter(Hole.number==i).filter(Hole.tee_id==tee.tee_id).one()
                append_item(hole, tee.holes)
                DBSession.commit()
              