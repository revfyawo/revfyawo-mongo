from tests.models import Author


def test_delete(connect, authors_collection, create_authors):
    author = Author.one()
    id = author.id
    author.delete()
    assert authors_collection.find_one({'_id': id}) is None
