import datetime
from typing import List

from revfyawo.mongo import Document

author_fields = {
    'username': str,
    'password': str,
    'articles': List[str],
    'created_at': datetime.datetime
}

article_fields = {
    'author': str,
    'slug': str,
    'title': str,
    'content': str,
    'seen': int,
    'created_at': datetime.datetime,
    'updated_at': datetime.datetime
}


class Author(Document):
    username: str
    password: str
    articles: List[str]
    created_at: datetime.datetime

    _collection = 'authors'


class Article(Document):
    author: str
    slug: str
    title: str
    content: str
    seen: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    _collection = 'articles'
