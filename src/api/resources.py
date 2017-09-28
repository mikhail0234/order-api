from tastypie.resources import ModelResource

from .models import Dish, Categories

class DishResource(ModelResource):
    class Meta:
        queryset = Dish.objects.all()
        resource_name = 'dish'



class CategoryResource(ModelResource):
    class Meta:
        queryset = Categories.objects.all()
        resource_name = 'category'




