from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('booking/create/', views.BookingCreateView.as_view()),
    path('booking/', views.BookingView.as_view()),
    path('booking/count/', views.BookingCountView.as_view()),
    path('booking/<int:pk>', views.SingleBookingView.as_view()),
    path('category/', views.CategoryView.as_view()),
    path('category/count/', views.CategoryCountView.as_view()),
    path('category/<int:pk>', views.SingleCategoryView.as_view()),
    path('menu-item/', views.MenuItemView.as_view()),
    path('menu-item/count/', views.MenuItemCountView.as_view()),
    path('menu-item/<int:pk>', views.SingleMenuItemView.as_view()),
    # path('cart-item/', views.CartItemView.as_view()),
    # path('cart-item/<int:pk>', views.SingleCartItemView.as_view()),
    # path('order/', views.OrderView.as_view()),
    # path('order/<int:pk>', views.SingleOrderView.as_view()),
    # path('order-item/', views.OrderItemView.as_view()),
    # path('order-item/<int:pk>', views.SingleOrderItemView.as_view()),
    # path('available-slot/', views.AvailableSlotView.as_view()),
    # path('available-slot/<int:pk>', views.SingleAvailableSlotView.as_view()),
    path('', views.ApiIndexView.as_view(), name='home'),
]
