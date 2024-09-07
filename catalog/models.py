from django.db import models
from datetime import datetime

NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    category_name = models.CharField(max_length=100, 
        verbose_name='название категории')
    description = models.TextField(
        )
    products_in_category = models.IntegerField(
        **NULLABLE)

    def __str__(self):
        return f'{self.pk} - {self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)

class Product(models.Model):
    product_name = models.CharField(
        max_length=100, 
        verbose_name='название продукта')
    product_description = models.TextField(
        )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE)
    product_image = models.ImageField(
        **NULLABLE)
    price = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        **NULLABLE)
    created_at = models.DateField(
        default=datetime.now)
    update_at = models.DateField(
        default=datetime.now)

    def __str__(self):
        return f'{self.product_name} стоит {self.price} находится в {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)

class Release(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='release',
        on_delete=models.CASCADE,
        verbose_name='Продукт',
        help_text='Выберите продукт',),

    version = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        help_text='Введите номер версии продукта',),

    version_name = models.CharField(
        max_length=100, 
        verbose_name='название версии',
        help_text='Введите имя версии продукта',),
        
    is_active = models.BooleanField(
        default=False,
        help_text='Укажите является ли версия активной',)

    def __str__(self):
        return f'{self.product.product_name} имеет версию {self.version} c именем {self.version_name} {"активная" if self.is_active else "неактивная"}'
    
    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = [-1]

