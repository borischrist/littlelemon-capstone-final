from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name',]
        
class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'inventory', 'category_id', 'category', 'photo']
        
class BookingSerializer(serializers.ModelSerializer):
    client_id = serializers.IntegerField(write_only=True)
    client = UserSerializer(read_only=True)
    
    class Meta:
        model = Booking
        fields = ['id', 'client_id', 'client', 'date', 'hour',]
        #fields = ['id', 'client', 'date', 'hour',]
        
# class AvailableSlotSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AvailableSlot
#         fields = ['id', 'amount', 'date', 'hour',]
        
# class CartItemSerializer(serializers.ModelSerializer):
#     client_id = serializers.IntegerField(write_only=True)
#     client = UserSerializer(read_only=True)
    
#     item_id = serializers.IntegerField(write_only=True)
#     item = MenuItemSerializer(read_only=True)
    
#     class Meta:
#         model = CartItem
#         fields = ['id', 'client_id', 'client', 'item_id', 'item', 'quantity',]
        
# class OrderSerializer(serializers.ModelSerializer):
#     client_id = serializers.IntegerField(write_only=True)
#     client = UserSerializer(read_only=True)
    
#     crew_id = serializers.IntegerField(write_only=True)
#     crew = UserSerializer(read_only=True)
    
#     class Meta:
#         model = Order
#         fields = ['id', 'status', 'crew_id', 'crew', 'client_id', 'client',]
        
# class OrderItemSerializer(serializers.ModelSerializer):    
#     item_id = serializers.IntegerField(write_only=True)
#     item = CartItemSerializer(read_only=True)
    
#     order_id = serializers.IntegerField(write_only=True)
#     order = OrderSerializer(read_only=True)
    
#     class Meta:
#         model = OrderItem
#         fields = ['id', 'item_id', 'item', 'order_id', 'order']