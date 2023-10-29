from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = 'restaurant'
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('menu', MenuView.as_view(), name="menu"),
    path('book', BookingView.as_view(), name="book"),
    path('contact', ContactView.as_view(), name="contact"),
    path('about', AboutView.as_view(), name="about"),
    path('api/', include('restaurant.api.urls')),
]
