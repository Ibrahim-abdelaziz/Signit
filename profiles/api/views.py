"""
connect endpoints with resources
"""

from flask import Blueprint
from flask_restful import Api

from profiles.api.resources import UserRegisterResource, UserResource

blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(blueprint)

api.add_resource(UserRegisterResource, "/user/")
api.add_resource(UserResource, "/users/<int:pk>/")
