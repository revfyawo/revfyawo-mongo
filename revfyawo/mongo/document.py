from typing import Optional, get_type_hints

from bson import ObjectId
from pymongo import MongoClient
from pymongo.collection import Collection

not_fields = ('_client', '_db', '_collection')


class Document:
    _id: Optional[ObjectId] = None

    _client: Optional[MongoClient] = None
    _db: str = ''
    _collection: str = ''

    class Meta:
        collection: Optional[Collection] = None
        fields = []

    @property
    def id(self) -> Optional[ObjectId]:
        return self._document.get('_id')

    @property
    def document(self) -> dict:
        return self._document

    def __init__(self, **kwargs):
        hints = get_type_hints(self.__class__)
        self.Meta.fields = list(filter(lambda x: x not in not_fields, hints))
        self._document = kwargs

    def __getattr__(self, item):
        if item in self.Meta.fields:
            return self._document.get(item)
        raise AttributeError

    def __setattr__(self, key, value):
        if key in self.Meta.fields:
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

        if not cls._collection:
            cls._collection = cls.__name__.lower()

        if cls._client and cls._db and cls._collection:
            cls.Meta.collection = cls._client[cls._db][cls._collection]

    def insert(self):
        return self.Meta.collection.insert_one(self._document)

    @classmethod
    def find_one(cls, filter_=None) -> Optional['Document']:
        doc = cls.Meta.collection.find_one(filter_)
        return cls(**doc) if doc else None

    def delete(self):
        return self.Meta.collection.find_one_and_delete({'_id': self.id})
