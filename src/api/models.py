from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Dish(models.Model):
    title = models.CharField(max_length=40)
    price = models.IntegerField()
    category = models.ForeignKey(Categories, default=id(0))

    def __str__(self):
        return self.title

def __str__(self):
    return '%s %d %s' % (self.title, self.price, self.category)

class Restaurant(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Order(models.Model):
    SHIRT_SIZES = (
        ('1', 'In Process'),
        ('2', 'Paid'),
        ('3', 'Finished'),
        ('4', 'Canceled'),

    )

    orderList = models.ManyToManyField(Dish)




    totalPrice = models.IntegerField('Цена:', default=0, editable=False)
    user = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    restaurant = models.ForeignKey(Restaurant)
    status = models.CharField(max_length=2, choices=SHIRT_SIZES, default=1)




