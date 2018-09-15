from datetime import datetime

import pytest
from pymongo import MongoClient

from revfyawo.mongo import Document

db_name = 'test_revfyawo_mongo'
db_client = MongoClient(serverSelectionTimeoutMS=1000)


@pytest.fixture(scope='session')
def connect():
    try:
        Document.connect(client=db_client, db=db_name)
        db_client.server_info()
    except Exception:
        raise
    db_client.drop_database(db_name)


@pytest.fixture
def author_dict():
    return {
        'username': 'root',
        'password': 'root',
        'created_at': datetime.now()
    }


@pytest.fixture
def authors_collection():
    return db_client[db_name]['authors']


@pytest.fixture
def create_authors(author_dict):
    db_client[db_name]['authors'].insert_one(author_dict)
