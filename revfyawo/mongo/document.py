from typing import Optional

from bson import ObjectId
from pymongo import MongoClient


class Document:
    _client: Optional[MongoClient] = None
    _db: str = ''
    _collection: str = __name__.lower()

    _id: Optional[ObjectId] = None

    @classmethod
    def set_client(cls, client: MongoClient):
        cls._client = client

    @classmethod
    def set_db_name(cls, db_name: str):
        cls._db = db_name

    def __init__(self, **kwargs):
        self._document = kwargs

    def insert(self):
        return self._client[self._db][self._collection].insert_one(self._document)

    @classmethod
    def one(cls, filter_=None):
        return cls._client[cls._db][cls._collection].find_one(filter_)
