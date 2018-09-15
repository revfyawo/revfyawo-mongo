import datetime
from typing import List

from revfyawo.mongo import Document, SubDocument


class BankInfo(SubDocument):
    iban: str
    credit_card: int
    credit_card_code: int
    credit_card_owner: str


class UserInfo(SubDocument):
    address: str
    bank_info: BankInfo
    description: str
    email: str
    job: str
    phone_number: str


class Author(Document):
    username: str
    password: str
    user_info: UserInfo
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


author_fields = {
    'username': str,
    'password': str,
    'user_info': UserInfo,
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
