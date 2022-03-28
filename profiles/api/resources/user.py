"""
user resources
"""
from http import HTTPStatus

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from profiles.api.schemas import UserSchema
from profiles.commons import utils
from profiles.commons.crud import CRUDMixin
from profiles.models import User



class UserResource(Resource, CRUDMixin):
    schema = UserSchema()
    

    def get(self, pk):
        user = User.query.get_or_404(pk)
        #return self.schema(exclude=self.schema.EXCLUDE_FOR_DUMP).dump(user)

        user = User.query.get_or_404(pk)
        return {"user": self.schema.dump(user).data}


    def patch(self, pk):
        user = User.query.get_or_404(pk)
        json_data = utils.get_json_from_request(request)
        try:
            user = self.schema().load(json_data, instance=user, partial=True)
        except ValidationError as errors:
            return {"errors": errors.messages}, HTTPStatus.BAD_REQUEST
        self.add(user)
        return self.schema(exclude=self.schema.EXCLUDE_FOR_DUMP).dump(user)


    


class UserRegisterResource(Resource, CRUDMixin):
    schema = UserSchema(many=False)

    def post(self):
        json_data = utils.get_json_from_request(request)

        try:
            user = self.schema().load(json_data)
        except ValidationError as errors:
            return {"errors": errors.messages}, HTTPStatus.BAD_REQUEST
        self.add(user)
        return self.schema(exclude=self.schema.EXCLUDE_FOR_DUMP).dump(user)

    def delete(self, pk):
        user = User.query.get_or_404(pk)
        super().delete(user)
        return "", HTTPStatus.NO_CONTENT