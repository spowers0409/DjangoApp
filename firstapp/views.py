from django.shortcuts import render
from django.http import HttpResponse

# This code tells django we have a web page or a view that takes
# as a parameter a request and returns a HttpResponse object
# The HttpResponse object is given an HTML test to give back to the calling browser.
def hello(request):
    text = """<h1>Hello World!</h1>"""
    return HttpResponse(text)

# Create your views here.
