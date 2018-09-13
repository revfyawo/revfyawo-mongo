from bson import ObjectId

from tests.models import Author


def test_find_one(create_authors):
    author = Author.one()
    assert isinstance(author.username, str)
    assert isinstance(author.id, ObjectId)
    author = Author.one({'username': 'revfyawo'})
    assert author is None
