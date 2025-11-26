from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu/', views.MenuItemsView, name='menu'),
    path('menu/items/<int:pk>', views.SingleMenuItemView, name='menu_item'),
    path('api-token-auth/', obtain_auth_token),
    path('booking/', views.book, name='book'),
    path('reservation/', views.reservations, name='reservations'),
    path('bookings/', views.bookings, name='bookings'),
]