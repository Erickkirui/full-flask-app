from flask_sqlalchemy import SQLAlchemy
from app import db

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<id: {self.id}, name: {self.name}, password: {self.password}, email: {self.email}>"
