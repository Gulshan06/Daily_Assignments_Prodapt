from django.db import models

# Create your models here.


class seller(models.Model):
    sname = models.CharField(max_length=50)
    sid = models.IntegerField()
    saddress =models.CharField(max_length=50)
    sphoneno = models.BigIntegerField()