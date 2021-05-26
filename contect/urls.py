from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('contactUs', views.contactUs),
    #path('home', views.home)
    
]