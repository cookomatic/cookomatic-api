"""Contains a database model for an Ingredient."""

from google.appengine.ext import ndb


class Ingredient(ndb.Model):
    """Models an ingredient."""
    name = ndb.StringProperty(required=True)

    # Amount of the ingredient
    amount = ndb.FloatProperty()

    # Unit of measurement: cups, mL, L, g, oz, etc.
    unit = ndb.StringProperty()

    @property
    def pretty(self):
        """Prints the ingredient as plain text."""
        string = "%s %s %s" % (self.amount, self.unit, self.name)
        return string.replace("None", "").strip()

    def serialize(self):
        """Serializes entity."""
        return self.to_dict()
