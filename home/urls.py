from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about_us',views.about_us,name='about_us'),
    path('contact_us',views.contact_us,name='contact_us'),
]