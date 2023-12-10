from django.urls import path
from .views import IndexView, AboutView, ProductDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
