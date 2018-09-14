import pytest

from tests.models import Author, author_fields


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


def test_correct_fields():
    author = Author()
    assert getattr(author, '_Document__fields') == ['_id'] + list(author_fields.keys())


def test_setattr(author_dict):
    author = Author(**author_dict)
    author.username = 'generated_username'
    assert author.document['username'] == 'generated_username'
