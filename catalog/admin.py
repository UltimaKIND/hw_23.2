from django.contrib import admin
from catalog.models import Product, Category, Release

# регистрация модели Product в панели администратора
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category')
    list_filter = ('category', )
    search_fields = ('product_name', 'description')

# регистрация модели Category в панели администратора
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')

# регистрация модели Release в панели администратора
@admin.register(Release)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version', 'version_name') 
