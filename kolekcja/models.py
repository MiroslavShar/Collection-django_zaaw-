from django.db import models
from django.contrib.auth.models import User, Group, Permission


class Type(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=64)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE,
                               null=True)
    def __str__(self):
        return self.name

class Metal(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Coin(models.Model):
    name = models.CharField(max_length=64)
    nominal = models.IntegerField
    type = models.ManyToManyField(Type)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    value = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class CollectionItem(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    condition = models.IntegerField() # od 1 do 10


