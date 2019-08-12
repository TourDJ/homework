from django.db import models
from arango import ArangoClient

# Create your models here.

# Create arangodb connect logic
def connectArangodb():
    client = ArangoClient(protocol='http', host='localhost', port=8529)
    db = client.db('homework', username='jiefang', password='jiefang')
    return db

def queryByAQL(aql):
    db = connectArangodb()
    cursor = db.aql.execute(aql)
    return cursor

MAX_LENGTH = 1000;

# Define basic model extends django mode, and own arangodb's
# common fileds. All ourself's model only extends it
class BaseMode(models.Model):
    _key = models.CharField(primary_key=True, max_length=1000)
    _id = models.CharField(max_length=1000)
    _rev = models.CharField(max_length=1000)

class Classwork(BaseMode):
    userId = models.IntegerField()
    title = models.CharField(max_length=MAX_LENGTH)

    def __str__(self):
        return '(Classwork: %d, %s)' % (self.userId, self.title)


class User(BaseMode):
    id = models.IntegerField()
    name = models.CharField(max_length=1000)

    def __str__(self):
        return '(User: %d, %s)' % (self.id, self.name)


