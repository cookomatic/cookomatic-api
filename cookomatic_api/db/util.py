"""General utilities for APIs."""

import flask


def generic_get(model, obj_id, convert_keys=None):
    """Generic API helper method to get an object by ID."""
    obj = model.get_by_id(obj_id)
    data = obj.to_dict()

    # Convert KeyProperty to ID if necessary
    if convert_keys:
        for key in convert_keys:
            data[key] = [a_key.id() for a_key in data[key]]

    # Send data
    return flask.jsonify(data)


def generic_save(model, name, convert_keys=None):
    """Generic API helper method to save an object."""
    data = flask.request.get_json()

    # Convert ID to KeyProperty if necessary
    if convert_keys:
        for key, convert_model in convert_keys.items():
            data[key] = [convert_model.get_by_id(item_id).key for item_id in data[key]]

    # Save data and return new ID
    key = model(**data).put()
    return flask.jsonify({'%s_id' % name: key.id()})
