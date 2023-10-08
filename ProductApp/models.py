from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    image_url = models.CharField(max_length=2000,null=True,blank=True)

    def __str__(self):
        return self.name

