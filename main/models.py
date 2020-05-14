from django.db import models


# Create your models here.
class Word(models.Model):
    list_id = models.CharField(max_length=100)
    word = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)


class List(models.Model):
    list_name = models.CharField(max_length=100)
    total_words = models.PositiveIntegerField(default=1)
    footer = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
