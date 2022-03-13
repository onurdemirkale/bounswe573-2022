from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, SWE573. Welcome to my Django project.")