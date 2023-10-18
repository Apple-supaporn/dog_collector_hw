from django.db import models


# Each Model is defined as a Python class that inherits from 'django.db.models.Model.'
# An ERD Entity maps to a 'Model' in Django, which maps to a 'table' in the database.


# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    favorite_toy = models.CharField(max_length=100, blank=True)


# add this // don't forget to migreate when update model/shegema
    def __str__(self):
        return self.name
