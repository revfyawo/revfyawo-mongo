import datetime

from revfyawo.mongo import Document
from tests.conftest import db_client, db_name
from tests.models import Author


def setup_module():
    Document.connect(client=db_client, db=db_name)


def teardown_module():
    db_client.drop_database(db_name)


def test_create(author_dict):
    author = Author(**author_dict)
    assert isinstance(author.username, str)
    assert isinstance(author.password, str)
    assert isinstance(author.created_at, datetime.datetime)
    assert author.id is None


def test_setattr(author_dict):
    author = Author(**author_dict)
    author.username = 'generated_username'
    assert author.document['username'] == 'generated_username'
