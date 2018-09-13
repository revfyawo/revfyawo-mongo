from revfyawo.mongo import Document
from tests.conftest import db_client, db_name
from tests.models import Author


def setup_module():
    Document.connect(client=db_client, db=db_name)


def teardown_module():
    db_client.drop_database(db_name)


def test_update(authors_collection, create_authors):
    author = Author.one()
    author.username = 'generated_username'
    author.update()
    updated = authors_collection.find_one({'username': 'generated_username'})
    assert updated['username'] == 'generated_username'
