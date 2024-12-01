from django.shortcuts import render
from django.http import HttpResponse

# views : when user access some url, this method will work

def say_hello(request):
    return HttpResponse("hello!")
