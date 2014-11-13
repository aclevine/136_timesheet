from gopher.models import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship

class Hole(Base):
    __tablename__ = 'holes'
    id = Column(Integer, primary_key=True)
    tee_id = Column(String, ForeignKey('tees.tee_id'), nullable= False)
    number = Column(Integer, nullable = False)
    par = Column(Integer, nullable = False)
    distance = Column(Integer, nullable = False)
    scores = relationship("Score", backref = 'hole')

    def __init__(self, number, tee_id, par, distance):
        self.tee_id = tee_id
        self.number = number
        self.par = par
        self.distance= distance

    def __repr__(self):
        return '<Hole %r>' % self.id

    def to_dict(self):
        return {
            "id": self.id,
            "tee_id": self.tee_id,
            "number": self.number,
            "par": self.par,
            "distance": self.distance
        }