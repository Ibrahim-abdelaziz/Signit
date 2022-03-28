"""
handle user scheme
"""
from marshmallow import fields

from profiles.commons import constants
from profiles.extensions import db, ma
from profiles.models import User
from profiles.validation import (EmailAlreadyExistValidator,
                                 FullNameLengthValidator, FullNameValidator,
                                 PasswordValidator)


class UserSchema(ma.ModelSchema):
    EXCLUDE_FOR_DUMP = ("password",)

    fullname = fields.String(
        required = True,
        validate = [FullNameValidator(constants.FULLNAME_REGX),FullNameLengthValidator(),],
    )
    email = fields.Email(validate=EmailAlreadyExistValidator())
    password = fields.String(
        required=True, validate=PasswordValidator(constants.PWD_REGEX),
    )

    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
