from django.conf.urls import url, include
from django.contrib import admin
from .resources import DishResource, CategoryResource, RestaurantResource, OrderResource, UserResource
from tastypie.api import Api




user_resource = UserResource()
dish_resource = DishResource()
category_resource = CategoryResource()
restaurant_resource = RestaurantResource()
order_resource = OrderResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(dish_resource.urls)),
    url(r'^api/', include(category_resource.urls)),
    url(r'^api/', include(restaurant_resource.urls)),
    url(r'^api/', include(order_resource.urls)),
    url(r'^api/', include(user_resource.urls)),

]
