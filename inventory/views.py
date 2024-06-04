from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello again, World")

def index(request):
    return render(request, 'inventory/index.html')

# Create your views here.
