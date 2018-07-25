## revfyawo.mongo

A python MongoDB ODM

### Get started

#### Define your model class

```python
from revfyawo.mongo import Document

class Dragon(Document):
    name: str
    health: int
```

#### Connect to the database

```python
from pymongo import MongoClient

Document.connect(MongoClient(), db='test')
```

#### Create and insert a document

```python
alduin = Dragon(name='Alduin', health=100)
alduin.insert()
```

#### Query the database

```python
alduin = Dragon.one({'name': 'Alduin'})
alive_dragons = Dragon.many({'health': {'$gt': 0}})
```


#### Update a document

```python
alduin.health = 50
alduin.update()
```

#### Delete a document

```python
alduin.delete()
```
