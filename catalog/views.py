from django.shortcuts import render, get_object_or_404
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, "catalog/index.html", {'products': products})

def about(request):
    return render(request, "catalog/about.html")

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "catalog/product_detail.html", {'product': product})