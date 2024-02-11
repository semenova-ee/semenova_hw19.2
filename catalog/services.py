from django.core.cache import cache
from .models import Category


def get_categories():
    # Попытаться получить категории из кеша
    categories = cache.get('categories')

    if not categories:
        # Если категории отсутствуют в кеше, выполнить запрос к базе данных
        categories = Category.objects.all()

        # Сохранить категории в кеше на 15 минут
        cache.set('categories', categories, timeout=60 * 15)

    return categories

