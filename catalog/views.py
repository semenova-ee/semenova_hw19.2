from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, "catalog/index.html", {'products': products})

def about(request):
    return render(request, "catalog/about.html")
