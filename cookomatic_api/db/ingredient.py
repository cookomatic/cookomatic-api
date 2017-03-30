"""Contains a database model for an Ingredient."""

from google.appengine.ext import ndb


class Ingredient(ndb.Model):
    """Models an ingredient."""
    name = ndb.StringProperty(required=True)

    # Amount of the ingredient
    amount = ndb.FloatProperty()

    # Unit of measurement: cups, mL, L, g, oz, etc.
    unit = ndb.StringProperty()
