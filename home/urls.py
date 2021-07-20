from django.contrib import admin
from django.urls import path
from home import views

app_name = 'user'
urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("signup/", views.sign_up, name='signup')
]