"""Contains a database model for a Dish."""

from google.appengine.ext import ndb


class Dish(ndb.Model):
    """Models a collection of steps that forms a single dish."""
    name = ndb.StringProperty(required=True)
    steps = ndb.KeyProperty(repeated=True)
