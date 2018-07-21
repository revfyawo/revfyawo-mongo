from typing import Optional, get_type_hints

from bson import ObjectId
from pymongo import MongoClient


not_fields = ('_client', '_db', '_collection')


class Document:
    _client: Optional[MongoClient] = None
    _db: str = ''
    _collection: str = __name__.lower()

    _id: Optional[ObjectId] = None

    class Meta:
        fields = []

    @classmethod
    def set_client(cls, client: MongoClient):
        cls._client = client

    @classmethod
    def set_db_name(cls, db_name: str):
        cls._db = db_name

    def __init__(self, **kwargs):
        self._document = kwargs
        type_hints = get_type_hints(self.__class__)
        self.Meta.fields = list(filter(lambda x: x not in not_fields, type_hints))

    def __getattr__(self, item):
        if item in self.Meta.fields:
            return self._document.get(item)

    def insert(self):
        return self._client[self._db][self._collection].insert_one(self._document)

    @classmethod
    def one(cls, filter_=None):
        return cls._client[cls._db][cls._collection].find_one(filter_)
