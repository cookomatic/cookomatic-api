"""General utilities for APIs."""

import flask


def ids_to_entities(data, props):
    """
    Takes a list of database IDs and gets the corresponding entities in-place.

    :param data: data to be converted. Usually output from flask.request.get_json.
    :param props: key-value list of property_name: entity_type. For example, {'steps': Step}
    :return: Entire data value with fields changed
    """
    for prop, model in props.items():
        data[prop] = [model.get_by_id(item_id).key for item_id in data[prop]]

    return data


def keys_to_ids(data, props):
    """
    Takes a list of database KeyProperty's and gets the corresponding IDs in-place.

    :param data: data to be converted.
    :param props: key-value list of property_name: entity_type. For example, {'steps': Step}
    :return: Entire entity with fields changed.
    """
    for key, model in props.items():
        data[key] = [generic_get(model, a_key.id()) for a_key in data[key]]

    return data


def generic_get(model, obj_id, convert_props=None):
    """Generic API helper method to get an object by ID."""
    obj = model.get_by_id(obj_id)
    data = obj.to_dict()

    # Convert KeyProperty to ID if necessary
    if convert_props:
        data = keys_to_ids(data, convert_props)

    # Send data
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
