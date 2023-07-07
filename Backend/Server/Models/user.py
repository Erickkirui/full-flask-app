from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import validates
import re
from app import db

class Users(db.Model):
    __tablename__ = 'users' 

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

   
    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email, "Email address must contain the @ symbol."
        assert '.' in email.split('@')[-1], "Email address must have a valid domain name."
        return email
    
    @validates('username')
    def validate_username(self, key, username):
        assert len(username) >= 8, "Username must be at least 8 characters long."
        return username
    
    @validates('password')
    def validate_password(self, key, password):
        assert any(char.isupper() for char in password), "Password must contain at least one capital letter."
        assert any(char.isdigit() for char in password), "Password must contain at least one number."
        assert re.search(r'[!@#$%^&*()-_=+{};:,<.>]', password), "Password must contain at least one symbol."
        return password
    
    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"
