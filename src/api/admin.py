from django.contrib import admin



# Register your models here.
from .models import Categories, Dish, Restaurant, Order

class CategoriesAdmin(admin.ModelAdmin):
     list_display = ["name"]
     class Meta:
         model = Categories


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["name"]

    class Meta:
        model = Restaurant


class DishAdmin(admin.ModelAdmin):
    list_display = ["title", "get_category", "price"]

    def get_category(self, obj):
        return obj.category.name

    class Meta:
        model = Dish


class OrderAdmin(admin.ModelAdmin):
    list_display = ["get_list", "get_price", "user", "created_at", "get_restaurant", "status"]

    def get_list(self, obj):
        return " ,\n".join([d.title +'-'+ str(d.price)+'₽ ' for d in obj.orderList.all()])

    def get_price(self, obj):
        total = 0
        for d in obj.orderList.all():
            total = total + d.price
        return total

    def get_restaurant(self, obj):
        return obj.restaurant.name

    class Meta:
        model = Order


admin.site.register(Restaurant, RestaurantAdmin)

admin.site.register(Categories, CategoriesAdmin)

admin.site.register(Dish, DishAdmin)

admin.site.register(Order, OrderAdmin)