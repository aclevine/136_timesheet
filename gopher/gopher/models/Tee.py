from gopher.models import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship

class Tee(Base):
    __tablename__ = 'tees'
    tee_id = Column(String, primary_key=True, unique=True)
    course_id = Column(String, ForeignKey('courses.course_id'), nullable = False)
    tee_name = Column(String, nullable = False)
    color = Column(String, nullable = False)
    par = Column(Integer, nullable = False)
    distance = Column(Integer, nullable = False)
    holes = relationship("Hole", backref = "tee")
    rounds = relationship("Round", backref = "tee")

    def __init__(self, tee_id, course_id, tee_name, color, par, distance):
        self.tee_id = tee_id
        self.course_id = course_id
        self.tee_name = tee_name
        self.color = color
        self.par = par
        self.distance= distance

    def __repr__(self):
        return '<Tee %r>' % self.tee_id

    def to_dict(self):
        return {
            "tee_id": self.tee_id,
            "course_id": self.course_id,
            "color": self.color,
            "tee_name": self.tee_name,
            "par": self.par,
            "distance": self.distance,
            "holes": [hole.id for hole in self.holes]
        }