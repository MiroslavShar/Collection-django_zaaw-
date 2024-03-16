from django.contrib import admin

# Register your models here.
from kolekcja.models import Category, Coin, Metal, Type

admin.site.register(Category)
admin.site.register(Coin)
admin.site.register(Type)
admin.site.register(Metal)
