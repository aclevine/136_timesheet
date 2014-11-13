from gopher.models import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship



class Club(Base):
    __tablename__ = 'clubs'
    facility_id = Column(String, primary_key=True, unique=True)
    facility_name = Column(String, nullable = False)
    number_of_holes = Column(Integer, nullable = False)
    address = Column(String, nullable = False)
    city = Column(String, nullable= False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable = False)
    website = Column(String, nullable= False)
    longitude = Column(Float, nullable = False)
    latitude = Column(Float, nullable = False)
    courses = relationship("Course", backref = "club")


    def __init__(self, facility_id, facility_name, address, city, state_id, website, longitude, latitude, number_of_holes=18):
        self.facility_id = facility_id
        self.facility_name = facility_name
        self.number_of_holes = number_of_holes
        self.address = address
        self.city = city
        self.state_id = state_id
        self.website = website
        self.longitude = longitude
        self.latitude = latitude

    def __repr__(self):
        return '<Club %r>' % self.facility_id

    def to_dict(self):
        return {
            "facility_id": self.facility_id,
            "facility_name": self.facility_name,
            "number_of_holes": self.number_of_holes,
            "address": self.address,
            "state": self.state.name,
            "city": self.city,
            "website": self.website,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "courses": [course.course_id for course in self.courses]
        }