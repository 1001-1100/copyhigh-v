from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class invEntry(models.Model):
    item = models.CharField(max_length=21)
    employee = models.IntegerField(default=0)
    beginv = models.IntegerField(default=0)
    endinv = models.IntegerField(default=0)
    actualinv = models.IntegerField(default=0)
    delivery = models.IntegerField(default=0)
    sales = models.IntegerField(default=0)
    salesamount = models.IntegerField(default=0)
    shortage = models.IntegerField(default=0)
    shortageamount = models.IntegerField(default=0)
    date = models.DateTimeField('Date Added', auto_now_add=True)

