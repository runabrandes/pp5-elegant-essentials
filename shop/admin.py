from django.contrib import admin
from .models import Product, Category

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name',)
    search_fields = ['product_name']
    list_filter = ('product_name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ['category_name']
    list_filter = ('category_name',)
