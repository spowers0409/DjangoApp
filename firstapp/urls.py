# What this code does is it checks the endpoint that you are trying to access
# in our case, it will be hello/
# We've declared a django path from the endpoiint 'hello' to the hello function defined in views
from django.urls import path, include
from . import views
urlpatterns = [
        path('hello/', views.hello, name = 'hello'),
]