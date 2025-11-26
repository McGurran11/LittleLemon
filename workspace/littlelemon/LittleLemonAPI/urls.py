from django.urls import path, include
from . import views
from .views import MenuItemsView, SingleMenuItemView
from restaurant.views import bookings
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('menu-items/', MenuItemsView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view(), name='single-menu-item'),
    path('message/', views.msg),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]