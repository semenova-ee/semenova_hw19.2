from django.contrib import admin
from django.db.models import Q

from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "category"]
    list_filter = ["category"]
    search_fields = ["name", "description"]

    def get_search_results(self, request, queryset, search_term):
        search_term_list = search_term.split(' ')

        if not any(search_term_list):
            return queryset, False

        name_query = Q(name__icontains=search_term)
        description_query = Q(description__icontains=search_term)
        queryset = queryset.filter(name_query | description_query)

        return queryset, False


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
