from datetime import datetime

import pytest
from pymongo import MongoClient

db_name = 'test_revfyawo_mongo'
db_client = MongoClient()


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
