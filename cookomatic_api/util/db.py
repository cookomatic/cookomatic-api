"""General utilities for APIs."""

import flask
from google.appengine.ext import ndb


def id_to_key(data, props):
    """
    Converts datastore IDs (integers) to Keys in-place.

    :param data: data to be converted. Usually output from flask.request.get_json.
    :param props: key-value list of property_name: entity_type. For example, {'steps': Step}
    :return: data with fields changed
    """

    def func(item_id, model):
        """Performs operation."""
        return ndb.Key(model, item_id)

    return _property_converter(data, props, func)


def key_to_id(data, props):
    """
    Converts datastore keys to IDs in-place.
    See id_to_key signature for details.
    """

    def func(item_key, _):
        """Performs operation."""
        return item_key.id()

    return _property_converter(data, props, func)


def key_to_entity(data, props):
    """
    Converts datastore keys to entities in-place.
    See id_to_key signature for details.
    """

    def func(item_key, _):
        """Performs operation."""
        return item_key.get()

    return _property_converter(data, props, func)


def entity_to_dict(data, props):
    """
    Converts entities to their dict representations in-place.
    See id_to_key signature for details.
    """

    def func(entity, _):
        """Performs operation."""
        return entity.serialize()

    return _property_converter(data, props, func)


def dict_to_entity(data, props):
    """
    Converts dicts to entities in-place.
    See id_to_key signature for details.
    """

    def func(item, model):
        """Performs operation."""
        return model(**item)

    return _property_converter(data, props, func)


def _property_converter(data, props, func):
    """Generic property converter to help the *_to_* functions above."""
    for key, val in props.items():
        if key in data:
            data[key] = [func(item, val) for item in data[key]]

    return data


def generic_save(model, name, data=None, extra_calls=None):
    """Generic API helper method to save an object."""
    if not data:
        data = flask.request.get_json()

    # Save data and return new ID
    entity = model(**data)

    if extra_calls:
        for call_name in extra_calls:
            getattr(entity, call_name)()

    key = entity.put()
    return flask.jsonify({'%s_id' % name: key.id()})


def remove_property(entity, prop):
    """Removes a property from an entity (if it exists)."""
    try:
        delattr(entity, prop)
    except TypeError:
        pass
