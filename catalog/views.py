from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "catalog/index.html")

def about(request):
    return render(request, "catalog/about.html")

