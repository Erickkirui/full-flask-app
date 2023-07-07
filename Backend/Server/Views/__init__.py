from flask import Blueprint
from flask_restful import Api
from Server.Views.user_views import UserListResource


Version_one = Blueprint('auth', __name__, url_prefix='/api/v1')
api = Api(Version_one)
api.add_resource(UserListResource, '/users')
