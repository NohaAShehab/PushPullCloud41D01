from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('Django Nohaaaaaaaa <html><body><h1> Hello World Ya nohaaaaaaa </body></html>')

