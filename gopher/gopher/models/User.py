import uuid
from gopher.models import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    uuid = Column(String)

    def __init__(self, email, password, isactive=True):
        self.email = email
        self.password = generate_password_hash(password)
        self.uuid = str(uuid.uuid4())
        self.isactive = isactive

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return self.uuid

    def is_authenticated(self):
        return True if self.uuid else False

    def is_anonymous(self):
        return False if self.uuid else True

    def __repr__(self):
        return '<User %r>' % self.email

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
        }