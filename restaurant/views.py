from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView
from .models import *
from .forms import BookingForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
    extra_context = {'page_title':'Home'}
    
class MenuView(ListView):
    model = MenuItem
    template_name = 'menu.html'
    extra_context = {'page_title':'Menu'}
    
class BookingView(FormView):
    template_name = 'booking.html'
    form_class = BookingForm
    extra_context = {'page_title':'Booking'}
    
class AboutView(TemplateView):
    template_name = 'about.html'
    extra_context = {'page_title':'About us'}
    
class ContactView(TemplateView):
    template_name = 'contact.html'
    extra_context = {'page_title':'Comtact us'}
    
    