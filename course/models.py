from django.db import models

# Create your models here.

class BaseMode(models.Model):
    _key = models.CharField(primary_key=True, max_length=1000)
    _id = models.CharField(max_length=1000)
    _rev = models.CharField(max_length=1000)


class Userinfo(BaseMode):
    id = models.IntegerField()
    name = models.CharField(max_length=1000)

    def __str__(self):
        return '(Userinfo: %d, %s)' % (self.id, self.name)


