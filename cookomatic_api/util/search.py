"""Search utilities."""

from google.appengine.api import search

NUM_SEARCH_RESULTS = 50


def create_index(index):
    """Creates a search index object."""
    return search.Index(name=index)


def create_document(entity, indexed_strings):
    """
    Creates a document based on entity.

    :param entity: entity to be indexed
    :param indexed_strings: key-value pair of strings that should be indexed (and tokenized)
    :return: Document representing entity
    """

    entity_id = str(entity.key.id())

    fields = [search.TextField(name='id', value=entity_id)]
    for name, string in indexed_strings.items():
        fields += tokenize_string(name, string)

    return search.Document(doc_id=entity_id, fields=fields)


def create_search_query(query_str):
    """Create search query object."""
    query_options = search.QueryOptions(limit=NUM_SEARCH_RESULTS)
    return search.Query(query_string=query_str, options=query_options)


def tokenize_string(name, string):
    """
    Tokenizes a string for indexing. For example, 'foo' would be ['f', 'fo', 'foo'].

    :param name: name of property
    :param string: string to be indexed
    :return: list of TextField objects of all tokens.
    """
    fields = []
    for i in range(1, len(string) + 1):
        fields.append(search.TextField(name=name, value=string[:i]))

    return fields


def results_to_entities(model, results):
    """
    Converts search results to their corresponding entities.

    :param model: entity model to convert to
    :param results: list of search results
    :return: list of entities
    """
    entities = []
    for result in results:
        entity_id = long(result.fields[0].value)
        entity = model.get_by_id(entity_id)
        entities.append(entity)

    return entities
