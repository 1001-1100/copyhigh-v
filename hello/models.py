from django.db import models
import pytz

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class invEntry(models.Model):

    item = models.CharField(max_length=21)
    employee = models.IntegerField(default=0)
    delivery = models.IntegerField(default=0)
    beginv = models.IntegerField(default=0)
    endinv = models.IntegerField(default=0)
    sales = models.IntegerField(default=0)
    salesamount = models.FloatField(default=0)
    actualinv = models.IntegerField(default=None, blank=True, null=True)
    shortage = models.IntegerField(default=None, blank=True, null=True)
    shortageamount = models.FloatField(default=None, blank=True, null=True)
    date = models.DateTimeField('Date Added', auto_now_add=True)

    def checkDate(self, currentDate):
        utc = pytz.UTC
        print(self.date)
        currentDate = currentDate.replace(tzinfo=utc) 
        entryDate = self.date.replace(tzinfo=utc) 
        return entryDate.year == currentDate.year and entryDate.month == currentDate.month and entryDate.day == currentDate.day 

class invItem(models.Model):
    item = models.CharField(max_length=21)
    price = models.FloatField(default=0)
    inv = models.IntegerField(default=0)

class user(models.Model):
    userid = models.CharField(max_length=21)
    password = models.CharField(max_length=21)


