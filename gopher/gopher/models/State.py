from gopher.models import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String, nullable = False, unique=True)
    clubs = relationship("Club", backref = "state")


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<State %r>' % self.name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "clubs": [club.facility_id for club in self.clubs],
        }