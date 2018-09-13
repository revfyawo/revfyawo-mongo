from .models import Author


def test_delete(authors_collection, create_authors):
    author = Author.one()
    id = author.id
    author.delete()
    assert authors_collection.find_one({'_id': id}) is None
