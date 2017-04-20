"""Contains a database model for Settings."""

from google.appengine.ext import ndb


class Settings(ndb.Model):
    """Models application settings."""
    google_client_id = ndb.StringProperty(required=True)

    @classmethod
    def get(cls):
        """Gets the Settings object from the database."""
        results = cls.query()

        if results.count() <= 0:
            raise ValueError(
                "No Settings found. Cannot continue.")
        elif results.count() > 1:
            raise RuntimeError(
                "Multiple Settings found. Cannot continue.")

        return results.fetch(1)[0]
