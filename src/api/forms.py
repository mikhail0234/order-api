# from django import forms
# from django.contrib.auth.models import User
#
# from .models import Dish, Categories
#
#
# class DishCategoryChoiceField(forms.ModelChoiceField):
#     def label_from_instance(self, obj):
#          return obj.get_full_name()
#
#
# class CategoryForm(forms.ModelForm):
#     category = DishCategoryChoiceField(queryset=Categories.objects.all())
#
#     class Meta:
#         model = Categories