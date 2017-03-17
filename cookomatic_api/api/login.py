"""Handle user login."""

import flask
from google.appengine.api import users

api_login = flask.Blueprint('api_login', __name__)


@api_login.route('/v1/login')
def login():
    """API method to log user in."""
    user = users.get_current_user()
    if user:
        nickname = user.nickname()
        logout_url = users.create_logout_url('/v1/login')
        return flask.jsonify({'user': nickname, 'logout_url': logout_url})
    else:
        login_url = users.create_login_url('/v1/login')
        return flask.redirect(login_url)
