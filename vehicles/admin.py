from django.contrib import admin
from .models import Category, Vehicle
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    ...
