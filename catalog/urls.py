from django.urls import path
from .views import index, about, product_detail

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]
