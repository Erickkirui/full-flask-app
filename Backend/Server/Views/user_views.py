from flask_restful import Resource
from Server.Models.user import Users

class UserListResource(Resource):
    def get(self):
        users = Users.query.all()
        user_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
        return {'users': user_list}, 200






