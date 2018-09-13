from bson import ObjectId

from tests.models import Author


def test_insert(author_dict):
    author = Author(**author_dict)
    author.insert()
    assert type(author.id) == ObjectId
