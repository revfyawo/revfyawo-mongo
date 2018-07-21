import pytest
from bson import ObjectId
from pymongo import MongoClient

from revfyawo.mongo.document import Document


class MongoDocument(Document):
    string: str
    integer: int

    _collection = 'mongo_document'


def setup_module():
    Document.connect(client=MongoClient(), db='test_revfyawo_mongo')


def teardown_module():
    MongoClient().drop_database('test_revfyawo_mongo')


@pytest.fixture
def document():
    return MongoDocument(string='string', integer=42)


def test_create(document):
    assert document.string == 'string'
    assert document.integer == 42
    assert document.id is None


def test_setattr(document):
    document.string = 'another string'
    assert document.document['string'] == 'another string'


def test_insert(document):
    document.insert()
    assert type(document.id) == ObjectId


def test_find_one():
    document = MongoDocument.one()
    assert document.string == 'string'
    assert isinstance(document.id, ObjectId)
    document = MongoDocument.one({'string': 'another string'})
    assert document is None


def test_update():
    document = MongoDocument.one()
    document.string = 'another string'
    document.update()
    assert MongoDocument.one().string == 'another string'


def test_delete():
    document = MongoDocument.one()
    id = document.id
    document.delete()
    assert MongoDocument.one({'_id': id}) is None
