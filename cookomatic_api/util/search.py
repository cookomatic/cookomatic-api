"""Search utilities."""

import json

from google.appengine.api import search

NUM_SEARCH_RESULTS = 50


def create_index(index):
    """Creates a search index object."""
    return search.Index(name=index)


def create_document(entity, attributes=None, indexed_attributes=None):
    """
    Creates a document based on entity.

    :param entity: entity to be indexed
    :param attributes: key-value pair of attr_name: field_type that should be in the document
    :param indexed_attributes: key-value pair of attr_name: field_type that should be indexed (and
    tokenized)
    :return: Document representing entity
    """

    entity_id = str(entity.key.id())

    # Create data field using normal attributes
    data = {'id': entity_id}
    if attributes:
        for name in attributes:
            data[name] = getattr(entity, name)

    # Create data field
    fields = [search.TextField(name='data', value=json.dumps(data))]

    # Create indexed attributes
    if indexed_attributes:
        for name, field_type in indexed_attributes.items():
            string = getattr(entity, name)
            fields += tokenize_string(name, string, field_type)

    return search.Document(doc_id=entity_id, fields=fields)


def create_search_query(query_str):
    """Create search query object."""
    query_options = search.QueryOptions(limit=NUM_SEARCH_RESULTS)
    return search.Query(query_string=query_str, options=query_options)


def tokenize_string(name, string, field_type):
    """
    Tokenizes a string for indexing. For example, 'foo' would be ['f', 'fo', 'foo'].

    :param name: name of property
    :param string: string to be indexed
    :param field_type: type of search field to use. For example, search.TextField.
    :return: list of TextField objects of all tokens.
    """
    fields = []
    for i in range(1, len(string) + 1):
        fields.append(field_type(name=name, value=string[:i]))

    return fields
