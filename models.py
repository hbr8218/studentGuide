from app import db
from sqlalchemy.dialects.postgresql import JSON

class Registration(db.Model):
    __tablename__ = 'registration'
    id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.String, nullable=False, unique=True)

class Login(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.Integer, nullable=False)