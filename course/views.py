from django.shortcuts import render
from django.http import HttpResponse
from arango import ArangoClient

from . import models

# Create your views here.

queryByAQL = models.queryByAQL

def index(request):
    classworks = []
    aql = 'FOR u IN hw_classwork RETURN u'
    cursor = queryByAQL(aql)
    for u in cursor:
        print(u)
        classwork = models.Classwork()
        classwork.userId = u['userId']
        classwork.title = u['title']
        classworks.append(classwork)
    print(classworks)
    return HttpResponse(classworks)
