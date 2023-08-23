from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=30)
    image = models.CharField(max_length=2000)

    def __str__(self):
        return self.categoryName
    

class item(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=280)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    image = models.CharField(max_length=2000)
    price = models.FloatField()

    def __str__(self):
        return self.title
    