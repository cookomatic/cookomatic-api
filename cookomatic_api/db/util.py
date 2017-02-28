"""General utilities for APIs."""

import flask


def generic_get(model, obj_id):
    """Generic API helper method to get an object by ID."""
    obj = model.get_by_id(obj_id)
    return flask.jsonify(obj.to_dict())


def generic_save(model, name, data):
    """Generic API helper method to save an object."""
    key = model(**data).put()
    return flask.jsonify({'%s_id' % name: key.id()})
