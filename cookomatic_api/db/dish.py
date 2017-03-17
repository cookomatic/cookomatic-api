"""Contains a database model for a Dish."""

import flask
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext import ndb

from cookomatic_api import util
from cookomatic_api.db.step import Step

GS_BUCKET = '/gs/project-cookomatic.appspot.com'
SEARCH_INDEX = 'dish'
THUMB_SIZE = 256

db_dish = flask.Blueprint('db_dish', __name__)


@db_dish.route('/v1/dish/<int:dish_id>')
def get_dish(dish_id):
    """API method to get a dish by ID."""
    return util.db.generic_get(Dish, dish_id, convert_keys=['steps'])


@db_dish.route('/v1/dish', methods=['POST'])
def save_dish():
    """API method to save a dish."""
    return util.db.generic_save(Dish, 'dish', convert_keys={'steps': Step},
                                extra_calls=['generate_img_url'])


@db_dish.route('/v1/dish/search')
def search_dish():
    """API method to search for a dish."""
    query_str = flask.request.args.get('search')
    return Dish.search(query_str)


class Dish(ndb.Model):
    """Models a collection of steps that form a single dish."""
    name = ndb.StringProperty(required=True)
    img_filename = ndb.StringProperty()
    img = ndb.StringProperty()
    img_thumb = ndb.StringProperty()
    tags = ndb.StringProperty(repeated=True)
    tools = ndb.StringProperty(repeated=True)
    ingredients = ndb.StringProperty(repeated=True)
    prep_list = ndb.StringProperty(repeated=True)
    steps = ndb.KeyProperty(repeated=True)
    total_time = ndb.IntegerProperty()
    serving_size = ndb.IntegerProperty()

    def generate_img_url(self):
        """Generates img urls for self.img and self.img_thumb based on self.img_filename."""
        # Transform image filename into serving_url
        if not self.img or not self.img_thumb:
            blob_key = blobstore.create_gs_key("%s/%s" % (GS_BUCKET, self.img_filename))
            self.img = images.get_serving_url(blob_key)
            self.img_thumb = images.get_serving_url(blob_key, size=THUMB_SIZE)

    @classmethod
    def _post_put_hook(cls, future):
        """Action right after an entity is saved."""
        entity = future.get_result().get()

        # Creating the new index
        index = util.search.create_index(SEARCH_INDEX)
        doc = util.search.create_document(entity, {'name': entity.name})
        index.put(doc)

    @classmethod
    def _pre_delete_hook(cls, key):
        """Action right before entity is deleted."""
        entity = key.get()

        # Delete search index
        index = util.search.create_index(SEARCH_INDEX)
        index.delete(str(entity.key.id()))

    @classmethod
    def search(cls, query_str):
        """Performs full-text search on entity index."""
        index = util.search.create_index(SEARCH_INDEX)
        query_obj = util.search.create_search_query(query_str)
        results = index.search(query=query_obj)

        entities = util.search.results_to_entities(cls, results)
        return flask.jsonify([entity.to_dict() for entity in entities])
