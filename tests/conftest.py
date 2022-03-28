import os
from functools import partial

import flask
import pytest

from profiles.app import create_app
from profiles.extensions import db as _db
from profiles.config import BASE_DIR

from .factories import users_factory


@pytest.fixture(scope="session")
def app():
    app = create_app()
    return app


@pytest.fixture(scope="session")
def db(app):
    _db.app = app

    with app.app_context():
        yield _db

    _db.session.close()


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client


@pytest.fixture(scope="session")
def root(app):
    return lambda *x: os.path.join(BASE_DIR, *x)


@pytest.fixture
def create_users(root):
    return users_factory(root)


@pytest.fixture
def users_url():
    return partial(flask.url_for, "api.userresource")


@pytest.fixture(scope="session")
def userinfo():
    return {
        "fullname": "Loen James",
        "email": "loen@test.com",
        "password": "test@LOEN4",
    }


@pytest.fixture(scope="session")
def default_headers():
    return {
        "Content-Type": "application/json",
    }


@pytest.fixture
def request_client(client, default_headers):
    for header, value in default_headers.items():
        client.environ_base[f"HTTP_{header.replace('-', '_').upper()}"] = value
    return client
