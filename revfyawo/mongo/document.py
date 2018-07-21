import logging
from typing import Optional, get_type_hints, List

from bson import ObjectId
from pymongo import MongoClient
from pymongo.collection import Collection

not_fields = ('_client', '_db', '_collection')


class Document:
    _id: Optional[ObjectId]

    _client: MongoClient
    _db: str
    _collection: str

    @property
    def id(self) -> Optional[ObjectId]:
        return self._document.get('_id')

    @property
    def document(self) -> dict:
        return self._document

    def __init__(self, **kwargs):
        hints = get_type_hints(self.__class__)
        self.__fields = list(filter(lambda x: x not in not_fields, hints))
        self.connect(self._client, self._db, self._collection)
        self._document = kwargs

    def __getattr__(self, item):
        if item in self.__fields:
            return self._document.get(item)
        raise AttributeError

    def __setattr__(self, key, value):
        if key == '_Document__fields':
            super(Document, self).__setattr__(key, value)
        if key in self.__fields:
            self._document[key] = value
        else:
            super(Document, self).__setattr__(key, value)

    @classmethod
    def connect(cls, client: Optional[MongoClient] = None,
                db: str = '', collection: str = ''):
        if client:
            cls._client = client
        if db:
            cls._db = db
        if collection:
            cls._collection = collection

        if not hasattr(cls, '_collection'):
            cls._collection = cls.__name__.lower()

    @classmethod
    def _get_collection(cls) -> Collection:
        return cls._client[cls._db][cls._collection]

    def insert(self):
        return self._get_collection().insert_one(self._document)

    @classmethod
    def one(cls, filter_=None) -> Optional['Document']:
        doc = cls._get_collection().find_one(filter_)
        return cls(**doc) if doc else None

    @classmethod
    def many(cls, filter_=None) -> List['Document']:
        docs = cls._get_collection().find(filter_)
        return [cls(**doc) for doc in docs]

    @classmethod
    def sample(cls, size: int) -> List['Document']:
        docs = cls._get_collection().aggregate([{'$sample': {'size': size}}])
        return [cls(**doc) for doc in docs]

    def update(self):
        return self._get_collection().find_one_and_replace({'_id': self.id}, self._document)

    def delete(self):
        return self._get_collection().find_one_and_delete({'_id': self.id})
