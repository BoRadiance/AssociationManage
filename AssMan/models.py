from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=256)
    date = models.CharField(max_length=256)
    content = models.TextField()

class Depart(models.Model):
    title = models.CharField(max_length=256)
    desc = models.TextField()

    def __str__(self):
        return self.title

class People(models.Model):
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=200,default='男')
    depart = models.ForeignKey(Depart,on_delete=models.CASCADE)
