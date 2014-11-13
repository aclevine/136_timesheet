from gopher.models import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float

class Score(Base):
    LEFT = "left"
    RIGHT = "right"
    FAIRWAY = "fairway"
    __tablename__ = 'scores'
    id = Column(Integer, primary_key=True)
    round_id = Column(Integer, ForeignKey('rounds.id'), nullable= False)
    hole_id = Column(Integer, ForeignKey('holes.id'), nullable= False)
    score= Column(Integer, nullable = False)
    putts = Column(Integer, nullable = False)
    gir = Column(Boolean, nullable = False)
    penalties = Column(Integer, nullable =False)
    drive= Column(String, nullable = False)

    def __init__(self, round_id, hole_id, score, putts, penalties, drive):
        self.round_id = round_id
        self.hole_id = hole_id
        self.score = score
        self.putts = putts
        self.penalties = penalties
        if score - putts <= self.hole.par:
            self.gir = True
        else:
           self.gir = False
        self.drive = drive

    def __repr__(self):
        return '<Score %r>' % self.id

    def to_dict(self):
        return {
            "id": self.id,
            "round_id": self.tee_id,
            "hole_id": self.hole_id,
            "score": self.score,
            "putts": self.putts,
            "penalties": self.penalties,
            "gir": self.gir,
            "drive": self.drive
        }