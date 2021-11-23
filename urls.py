from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/', home, name="home"),
    path('api/<int:id>', home),
    path('api/update/<int:id>', update, name="update"),
    # path('api/<int:pk>', update, name="home"),

]
