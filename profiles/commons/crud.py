
"""Default Crud Methods """

from profiles.extensions import db


class CRUDMixin:
    def add(self, resource):
        db.session.add(resource)
        self.save()

    def delete(self, resource):
        db.session.delete(resource)
        self.save()

    @staticmethod
    def save():
        db.session.commit()
