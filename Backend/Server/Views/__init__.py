from flask import Blueprint
from flask_restful import Api
from Server.Views.user_views import UserResources,GetAllUsers


Version_one = Blueprint('auth', __name__, url_prefix='/api/v1')
api = Api(Version_one)
api.add_resource(GetAllUsers, '/users')
api.add_resource(UserResources, '/users/<int:user_id>')

