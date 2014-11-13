from gopher.models import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship

class Round(Base):
    __tablename__ = 'rounds'
    id = Column(Integer, primary_key=True)
    tee_id = Column(String, ForeignKey('tees.tee_id'), nullable= False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable = False)
    total_score= Column(Integer, nullable = False)
    scores = relationship("Score", backref = 'Round')

    def __init__(self, tee_id, total_score, user_id):
        self.tee_id = tee_id
        self.total_score = total_score
        self.user_id = user_id

    def __repr__(self):
        return '<Round %r>' % self.id

    def to_dict(self):
        return {
            "id": self.id,
            "tee_id": self.tee_id,
            "total_score": self.total_score,
            "user_id": self.user_id
        }