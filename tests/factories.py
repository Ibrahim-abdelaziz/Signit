import json

from profiles.commons.utils import read_from_file
from profiles.extensions import db
from profiles.models import User


def users_factory(root):
    users_data = json.loads(read_from_file(root("tests", "fixtures", "users.json")))
    list_of_users = [User(**user) for user in users_data]
    db.session.add_all(list_of_users)
    db.session.commit()
    return list_of_users
