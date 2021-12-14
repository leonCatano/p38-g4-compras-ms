from django.db import models

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    user= models.IntegerField()
    balance = models.IntegerField(default=0)
    lastChangeDate = models.DateTimeField()
    isActive = models.BooleanField(default=True)
