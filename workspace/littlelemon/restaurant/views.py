from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.decorators import api_view
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()          # Defines the data source
    serializer_class = MenuSerializer      # Defines how data is converted to/from JSON

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()          # Defines the data source
    serializer_class = MenuSerializer      # Defines how data is converted to/from JSON

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer