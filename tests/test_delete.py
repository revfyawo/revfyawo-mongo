from revfyawo.mongo import Document
from tests.conftest import db_client, db_name
from tests.models import Author


def setup_module():
    Document.connect(client=db_client, db=db_name)


def teardown_module():
    db_client.drop_database(db_name)


def test_delete(authors_collection, create_authors):
    author = Author.one()
    id = author.id
    author.delete()
    assert authors_collection.find_one({'_id': id}) is None
