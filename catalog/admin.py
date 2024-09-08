from django.contrib import admin
from catalog.models import Product, Category, Release

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category')
    list_filter = ('category', )
    search_fields = ('product_name', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')

@admin.register(Release)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version', 'version_name') 
