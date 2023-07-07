from flask_restful import Resource
from Server.Models.user import Users
from flask import request
from app import db
import bcrypt


class GetAllUsers(Resource):
    def get(self):
        users = Users.query.all()
        user_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
        return {'users': user_list}, 200
    
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return {'message': 'Invalid data. Please provide username, email, and password.'}, 400
        

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        new_user = Users(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User created successfully'}, 201
    
    
    

class UserResources(Resource):
    def get(self, user_id):
        user = Users.query.get(user_id)
        if user:
            user_data = {'id': user.id, 'username': user.username, 'email': user.email}
            return {'user': user_data}, 200
        else:
            return {'message': 'User not found'}, 404
        


    def patch(self, user_id):
        user = Users.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        data = request.get_json()
        username = data.get('username')
        email = data.get('email')

        if username:
            user.username = username
        if email:
            user.email = email

        db.session.commit()

        return {'message': 'User updated successfully'}, 200
    
    def delete(self, user_id):
        user = Users.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        db.session.delete(user)
        db.session.commit()

        return {'message': 'User deleted successfully'}, 200
        

    
