from django.db import models

#username = Yeamin(for admin)
#email = yeamin@gmail.com
#pass = 123456

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=10000)
    summary = models.TextField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title






