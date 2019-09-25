from django.db import models


class Book(models.Model):
    name= models.CharField(max_length=200)
    pageNumber= models.IntegerField()
    genre= models.CharField(max_length=100)
    publishDate = models.DateTimeField('date published')



