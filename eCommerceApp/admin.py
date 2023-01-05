from django.contrib import admin
from .models import Products


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ("user", "title", "price", "image",)

# Register your models here.
admin.site.register(Products)

