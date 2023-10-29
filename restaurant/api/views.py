from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.generic.base import TemplateView
from django.http import QueryDict
from .serializers import *
from ..models import *
from pprint import pprint

class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    
    def create(self, request, *args, **kwargs):
        if isinstance(request.data, QueryDict): # optional
            request.data._mutable = True
        request.data['client_id'] = request.user.id
        print(request.user)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
      

class BookingView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    authentication_classes = [SessionAuthentication]
    
    def get_queryset(self):
        date = self.request.GET.get('date')
        if date is None:
            return self.queryset
        else:
            return Booking.objects.filter(date=date)
    
class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer



class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class SingleCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer   

    search_fields = ['$name']
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class CountModelMixin(APIView):
    renderer_classes = (JSONRenderer, )
    model = object
    
    def get(self, request, format=None):
        count = self.model.objects.count()
        content = {'count': count}
        return Response(content)
    
class MenuItemCountView(CountModelMixin):
    model = MenuItem
class CategoryCountView(CountModelMixin):
    model = Category
class BookingCountView(CountModelMixin):
    model = Booking

class ApiIndexView(TemplateView):
    template_name = "api.index.html"