from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi 2:00 class!!! Hello, world. You're at the textbook exchange index.  Cool test!  Yes it is!")
