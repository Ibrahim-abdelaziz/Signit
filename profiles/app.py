"""
init app configuration
"""

from flask import Flask

from profiles.api import views
from profiles.config import SQLALCHEMY_DATABASE_URI
from profiles.extensions import db, migrate



def create_app(config=None, testing=False):
    """Application factory, used to create application
    """

    app = Flask(__name__)
    configure_app(app)
    configure_extensions(app)
    register_blueprints(app)  # domain/api/

    return app


def configure_app(app, testing=False):
    """set configuration for application"""

    app.config.from_object("profiles.config.develop")

    if testing is True:
        # override with testing config
        app.config.from_object("profiles.config.test")

    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.url_map.strict_slashes = False


def configure_extensions(app):
    """configure flask extensions"""
    
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    """register all blueprints for application"""
    app.register_blueprint(views.blueprint)


def register_shellcontext(app):
    """Register shell context objects."""

    def shell_context():
        """Shell context objects."""
        return {"db": db}

    app.shell_context_processor(shell_context)
