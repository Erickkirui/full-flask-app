# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import func
# from sqlalchemy.orm import validates
# import re
# from app import db


# class Customer(db.Model):
#     __tablename__ = 'customers'

#     id = db.Column(db.Integer, primary_key=True)
#     customer_name = db.Column(db.String(20), unique=True, nullable=False)

#     transactions = db.relationship("Transaction", back_populates="customer")


#     @validates('username')
#     def validate_username(self, key, username):
#         assert len(username) >= 8, "Username must be at least 8 characters long."
#         return username
    
#     def __repr__(self):
#         return f"id : {self.id} name: {self.customer_name}"
    
# class Transactions(db.Model):
#     __tablename__ = 'transactions'

#     id = db.Column(db.Integer, primary_key=True)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
#     point = db.Column(db.Integer)
    
#     customer = db.relationship("Customer", back_populates="transactions")

# class LoyaltyPoints(db.Model):
#     __tablename__ = 'loyaltypoints'

#     id = db.Column(db.Integer, primary_key=True)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
#     point = db.Column(db.Integer)



