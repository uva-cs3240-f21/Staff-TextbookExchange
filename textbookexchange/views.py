from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi 11:00!!! You are my besties.  Don't tell 2:00.  I'll delete this from the recording.  Hello, world. You are my everything!  :heart:")
