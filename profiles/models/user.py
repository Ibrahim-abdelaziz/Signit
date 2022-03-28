# Database models file

from profiles.commons.crud import CRUDMixin
from profiles.extensions import db, pwd_context
from sqlalchemy import asc



class User(db.Model, CRUDMixin):
    """Basic user model"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = pwd_context.hash(self.password)

    def __repr__(self):
        return f"[user {self.id}-{self.fullname}]"


    @classmethod
    def get_fullname_by_asc(cls):
        return cls.query.order_by(asc(User.fullname))

