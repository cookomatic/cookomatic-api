"""Contains a database model for a User."""

import logging

from google.appengine.ext import ndb


class User(ndb.Model):
    """Models a User of this application."""
    email = ndb.StringProperty(required=True)

    @classmethod
    def get_by_email(cls, email):
        """Gets User from database given an email address. If no User found, one is created."""
        results = User.query(User.email == email)

        if results.count() <= 0:
            logging.info("Creating new user with email: %s", email)
            new_user = cls(email=email)
            new_user.put()
            return new_user

        elif results.count() > 1:
            raise RuntimeError(
                "Found multiple Users with email: %s. "
                "Cannot continue." % email)

        # If user found, return object
        return results.fetch(1)[0]
