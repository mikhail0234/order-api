from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from django.contrib.auth.models import User

from .models import Dish, Categories, Restaurant, Order



class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        excludes = ['email', 'password', 'is_staff', 'is_superuser']

        authorization = DjangoAuthorization()
        authentication = BasicAuthentication()
        always_return_data = True
        default_format = "application/json"

class DishResource(ModelResource):
    class Meta:
        queryset = Dish.objects.all()
        resource_name = 'dish'


class CategoryResource(ModelResource):
    class Meta:
        queryset = Categories.objects.all()
        resource_name = 'category'


class RestaurantResource(ModelResource):
    class Meta:
        queryset = Restaurant.objects.all()
        resource_name = 'restaurant'

class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'







