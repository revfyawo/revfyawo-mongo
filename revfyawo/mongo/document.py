from typing import Optional, get_type_hints

from bson import ObjectId
from pymongo import MongoClient


class Document:
    _id: Optional[ObjectId] = None

    class Meta:
        client: Optional[MongoClient] = None
        db: str = ''
        collection: str = __name__.lower()
        fields = []

    @property
    def id(self) -> Optional[ObjectId]:
        return self._document.get('_id')

    def __init__(self, **kwargs):
        self.Meta.fields = get_type_hints(self.__class__)
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

    def insert(self):
        return self.Meta.client[self.Meta.db][self.Meta.collection].insert_one(self._document)

    @classmethod
    def find_one(cls, filter_=None) -> Optional['Document']:
        doc = cls.Meta.client[cls.Meta.db][cls.Meta.collection].find_one(filter_)
        return cls(**doc) if doc else None

    def delete(self):
        return self.Meta.client[self.Meta.db][self.Meta.collection].find_one_and_delete({'_id': self.id})
