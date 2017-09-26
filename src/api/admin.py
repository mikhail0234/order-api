from django.contrib import admin


# Register your models here.
from .models import Categories, Dish

class CategoriesAdmin(admin.ModelAdmin):
     list_display = ["name"]
     class Meta:
         model = Categories


class DishAdmin(admin.ModelAdmin):
    list_display = ["title", "get_category", "price"]

    def get_category(self, obj):
        return obj.category.name

    class Meta:
        model = Dish


admin.site.register(Categories, CategoriesAdmin)

admin.site.register(Dish, DishAdmin)