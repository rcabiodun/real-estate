
from .views import *
from django.urls import path

urlpatterns = [
    path('', home,name="home"),
    path('contact', contact,name="contact"),
    path('about', about,name="about"),
    path('gallery', gallery,name="gallery"),
    path('properties', properties,name="properties"),
    path('services', services,name="services"),

]
