from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=65)


class Vehicle(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    kilometers = models.IntegerField()
    kilometers_unit = models.CharField(max_length=65)
    year = models.IntegerField()
    year_time_unit = models.CharField(max_length=65)
    vehicle_description = models.TextField()
    vehicle_description_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()
    cover = models.ImageField(upload_to='recipes/covers/%Y%/%m%/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
