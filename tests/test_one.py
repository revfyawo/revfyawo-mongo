from bson import ObjectId

from revfyawo.mongo import Document
from tests.conftest import db_client, db_name
from tests.models import Author


def setup_module():
    Document.connect(client=db_client, db=db_name)


def teardown_module():
    db_client.drop_database(db_name)


def test_find_one(create_authors):
    author = Author.one()
    assert isinstance(author.username, str)
    assert isinstance(author.id, ObjectId)
    author = Author.one({'username': 'revfyawo'})
    assert author is None
