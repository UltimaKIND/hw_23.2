from django.core.cache import cache
from catalog.models import Product
from config.settings import CACHES_ENABLED


def get_products_from_cache():
    '''
    Получает данные по продуктам из кеша, если кеш пуст, получает данные из бд
    '''
    if not CACHES_ENABLED:
        return Product.objects.all()
    key = 'product_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products
