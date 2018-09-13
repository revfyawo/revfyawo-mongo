import datetime

from .models import Author


def test_create(author_dict):
    author = Author(**author_dict)
    assert isinstance(author.username, str)
    assert isinstance(author.password, str)
    assert isinstance(author.created_at, datetime.datetime)
    assert author.id is None


def test_setattr(author_dict):
    author = Author(**author_dict)
    author.username = 'generated_username'
    assert author.document['string'] == 'generated_username'
