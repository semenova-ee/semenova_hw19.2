from django.http import HttpResponse

def index(request):
    return HttpResponse('Katya')

def about(request):
    return HttpResponse('<h1>about</h1>')
