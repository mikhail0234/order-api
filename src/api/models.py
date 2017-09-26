from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=40)

def __str__(self):
    return '%s' % (self.name)

class Dish(models.Model):
    title = models.CharField(max_length=40)
    price = models.IntegerField()
    category = models.ForeignKey(Categories)

def __str__(self):
    return '%s %d %s' % (self.title, self.price, self.category)


