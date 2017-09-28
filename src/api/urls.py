from django.conf.urls import url, include
from django.contrib import admin
from .resources import DishResource, CategoryResource
dish_resource = DishResource()
category_resource = CategoryResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(dish_resource.urls)),
    url(r'^api/', include(category_resource.urls)),
]
