from django.db import models
from django.utils import timezone

# Create your models here.
class Gender(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=100)
    b_date = models.DateField(default=timezone.now())
    Gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Actor/')
    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)
    b_date = models.DateField(default=timezone.now())
    Gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Director/')
    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    r_date = models.DateField(default=timezone.now())
    directors = models.ManyToManyField(Director)
    actors = models.ManyToManyField(Actor)
    def __str__(self):
        return self.name

