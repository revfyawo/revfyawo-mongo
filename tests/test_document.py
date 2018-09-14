import pytest

from revfyawo.mongo import Document
from tests.conftest import db_client, db_name
from tests.models import Author


def setup_module():
    Document.connect(client=db_client, db=db_name)


def teardown_module():
    db_client.drop_database(db_name)


def test_create_kwargs(author_dict):
    author = Author(**author_dict)
    assert author.document == author_dict
    assert author.id is None


def test_create_document(author_dict):
    author = Author(author_dict)
    assert author.document == author_dict
    assert author.id is None


def test_create_bot_kwargs_document(author_dict):
    with pytest.raises(AttributeError):
        author = Author(author_dict, **author_dict)


def test_setattr(author_dict):
    author = Author(**author_dict)
    author.username = 'generated_username'
    assert author.document['username'] == 'generated_username'
