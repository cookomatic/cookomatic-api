"""Provides utilities for the API functions like authentication and serialization."""

import logging
from functools import wraps
import os

import flask
from oauth2client import client, crypt

from cookomatic_api.db.settings import Settings
from cookomatic_api.db.user import User

TEST_USER_EMAIL = 'test@example.com'
UNAUTHORIZED = ('', 401)


def _in_production():
    """Reads environment and determines if this instance is running in production."""
    return os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/')


def _get_test_user():
    """Returns a user that is used for testing API calls."""
    # If there is a user in the database, return the first one
    if User.query().count() >= 1:
        return User.query().fetch(1)[0]

    # Otherwise, create a new test user
    user = User(email=TEST_USER_EMAIL)
    user.put()
    return user


def authenticate(api_func):
    """Validates authorization token and, if valid, returns user data to API call."""

    @wraps(api_func)
    def decorated_function(*args, **kwargs):
        """Inner function for authenticate decorator."""
        # If not in production, bypass authentication and get a default user
        if not _in_production():
            user = _get_test_user()
            return api_func(user, *args, **kwargs)

        token = flask.request.headers.get('X-AUTHORIZATION')
        if not token:
            return UNAUTHORIZED

        try:
            # Validate Google auth token
            client_id = Settings.get().google_client_id
            auth_info = client.verify_id_token(token, client_id)

            if auth_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise crypt.AppIdentityError("Wrong token issuer.")

            # We're authenticated, so get user data and call the real API method
            user = User.get_by_email(auth_info['email'])
            logging.info('Logging in user with email: %s', auth_info['email'])
            return api_func(user, *args, **kwargs)

        except crypt.AppIdentityError:
            return UNAUTHORIZED

    return decorated_function


def generic_save(model, data=None, extra_calls=None):
    """Generic API helper method to save an object."""
    if not data:
        data = flask.request.get_json()

    # Save data and return new ID
    entity = model(**data)

    if extra_calls:
        for call_name in extra_calls:
            getattr(entity, call_name)()

    entity.put()
    return flask.jsonify(entity.serialize())
