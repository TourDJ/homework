from django.shortcuts import render
from django.http import HttpResponse
from arango import ArangoClient

from . import models

# Create your views here.

def connectArangodb():
    client = ArangoClient(protocol='http', host='localhost', port=8529)
    db = client.db('homework', username='jiefang', password='jiefang')
    return db

def queryByAQL(aql):
    db = connectArangodb()
    cursor = db.aql.execute(aql)
    return cursor

def index(request):
    users = []
    cursor = queryByAQL('FOR u IN hw_user RETURN u')
    for u in cursor:
        print(u)
        user = models.Userinfo()
        user.name = u['name']
        user.id = u['id']
        users.append(user)
    print(users)
    return HttpResponse('Hello, world.')
