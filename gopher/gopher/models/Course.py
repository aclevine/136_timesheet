from gopher.models import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'courses'
    course_id = Column(String, primary_key=True, unique=True)
    facility_id = Column(String, ForeignKey('clubs.facility_id'), nullable = False)
    course_name = Column(String, nullable = False)
    holes = Column(Integer, nullable = False)
    par = Column(Integer, nullable = False)
    course_architect = Column(String, nullable = False)
    open_date = Column(Integer, nullable = False)
    tees = relationship("Tee", backref = "course")


    def __init__(self, course_id, facility_id, course_name, holes, par, course_architect, open_date):
        self.course_id = course_id
        self.facility_id = facility_id
        self.course_name = course_name
        self.holes = holes
        self.par = par
        self.course_architect = course_architect
        self.open_date = open_date

    def __repr__(self):
        return '<Course %r>' % self.course_id

    def to_dict(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "facility_id": self.facility_id,
            "holes": self.holes,
            "par": self.par,
            "course_architect": self.course_architect,
            "open_date": self.open_date,
            "tees": [tee.id for tee in self.tees]
        }