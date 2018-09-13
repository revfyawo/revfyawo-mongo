from .models import Author


def test_update(authors_collection, create_authors):
    author = Author.one()
    author.username = 'generated_username'
    author.update()
    updated = authors_collection.find_one({'username': 'generated_username'})
    assert updated['username'] == 'generated_username'
