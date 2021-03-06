"""Contains a database model for a Dish."""

import json
import random

import flask
from google.appengine.api import search
from google.appengine.ext import ndb

from cookomatic_api import util
from cookomatic_api.db.ingredient import Ingredient
from cookomatic_api.db.step import Step

SEARCH_INDEX = 'dish'
db_dish = flask.Blueprint('db_dish', __name__)


@db_dish.route('/v1/dish/<int:dish_id>')
@util.api.authenticate
def get_dish(user, dish_id):
    """API method to get a dish by ID."""
    obj = Dish.get_by_id(dish_id)
    return flask.jsonify(obj.serialize())


@db_dish.route('/v1/dish', methods=['POST'])
@util.api.authenticate
def save_dish(user):
    """API method to save a dish."""
    data = flask.request.get_json()
    data['owner'] = user.key

    # Deserialize properties
    data = util.db.dict_to_entity(data, {'ingredients': Ingredient})
    data = util.db.id_to_key(data, props={'steps': Step})

    return util.api.generic_save(Dish, data=data, extra_calls=['generate_img_url'])


@db_dish.route('/v1/dish/search')
@util.api.authenticate
def search_dish(user):
    """API method to search for a dish."""
    query_str = flask.request.args.get('search')
    return flask.jsonify(Dish.search(query_str))


@db_dish.route('/v1/dish/suggested')
@util.api.authenticate
def suggest_dish(user):
    """API method recommend a dish to go along with the current one."""
    all_dishes = Dish.search('')
    return flask.jsonify(random.sample(all_dishes, 2))


class Dish(ndb.Expando):
    """Models a collection of steps that form a single dish."""
    name = ndb.StringProperty(required=True)
    owner = ndb.KeyProperty()

    # Image filename as stored on Google Cloud Storage
    img_filename = ndb.StringProperty()

    # Full-sized image URL
    img = ndb.StringProperty()

    # Thumbnail image URL
    img_thumb = ndb.StringProperty()

    # List Ingredients required by this dish
    ingredients = ndb.StructuredProperty(Ingredient, repeated=True)

    # Tags for this dish (is searchable)
    tags = ndb.StringProperty(repeated=True)

    # Tools required to complete this dish (pots, pans, etc.)
    tools = ndb.StringProperty(repeated=True)

    # Things that the user needs to do before starting cooking
    prep_list = ndb.StringProperty(repeated=True)

    # List of Step keys
    steps = ndb.KeyProperty(repeated=True)

    # How many people this dish feeds
    serving_size = ndb.IntegerProperty()

    @property
    def estimated_time(self):
        """Return an estimate for how much time this dish takes."""
        estimated_time = 0
        for step_key in self.steps:
            step = step_key.get()
            estimated_time += step.estimated_time

        return estimated_time

    def generate_img_url(self):
        """
        Generates img urls for self.img and self.img_thumb based on self.img_filename.
        :return: None
        """
        # Transform image filename into serving_url
        if not self.img or not self.img_thumb:
            self.img, self.img_thumb = util.images.generate_image_url(self.img_filename)

    def parse_step_deps(self):
        """
        Converts tmp_depends_on to depends_on and tmp_steps to steps. Also puts each step in DB and
        saves keys to self.depends_on.

        :return: None
        """
        self.steps = []
        for step in self.tmp_steps:
            try:
                # Convert each dep from list index to key
                step.depends_on = []
                for dep_idx in step.tmp_depends_on:
                    step.depends_on.append(self.steps[dep_idx])

            except AttributeError:
                pass

            # Remove tmp property
            util.db.remove_property(self, 'tmp_depends_on')

            # Put Step in DB and save key in self.steps
            self.steps.append(step.put())

        # Remove tmp property
        util.db.remove_property(self, 'tmp_steps')

    @classmethod
    def search(cls, query_str):
        """Performs full-text search on entity index."""
        index = util.search.create_index(SEARCH_INDEX)
        query_obj = util.search.create_search_query(query_str)
        results = index.search(query=query_obj)

        serialized_results = [json.loads(result.fields[0].value) for result in results]
        return serialized_results

    @classmethod
    def _post_put_hook(cls, future):
        """Action right after an entity is saved."""
        entity = future.get_result().get()

        # Creating the new index
        index = util.search.create_index(SEARCH_INDEX)
        doc = util.search.create_document(
            entity,
            attributes=['name', 'img', 'img_thumb'],
            indexed_attributes={
                'name': search.TextField
            })
        index.put(doc)

    @classmethod
    def _pre_delete_hook(cls, key):
        """Action right before entity is deleted."""
        entity = key.get()

        # Delete all Step objects
        for step_key in entity.steps:
            step_key.delete()

        # Delete search index
        index = util.search.create_index(SEARCH_INDEX)
        index.delete(str(entity.key.id()))

    def serialize(self):
        """Serializes entity."""
        data = self.to_dict()
        data['id'] = self.key.id()

        # Serialize properties
        data = util.db.key_to_entity(data, {'steps': None})
        data = util.db.entity_to_dict(data, {'steps': None})
        data['ingredients'] = [ingred.pretty for ingred in self.ingredients]
        data['estimated_time'] = self.estimated_time
        data['owner'] = data['owner'].id() if data['owner'] else None

        return data
