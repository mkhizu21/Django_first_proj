from django.contrib import admin
from django.urls import path
from firstapp import views
urlpatterns = [
   path("", views.index, name='index'),
   path("about", views.about, name='about'),
   path("services", views.services, name='services'),
   path("contact", views.contact, name='contact'),
]

#https://source.unsplash.com/1600x600/?kids,clothes