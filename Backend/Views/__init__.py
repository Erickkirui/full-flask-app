from flask import Blueprint
# from user_views import *

Version_one = Blueprint( 'auth',
    __name__,
    url_prefix='/api/v1'
)