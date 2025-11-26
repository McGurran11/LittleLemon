from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm
from rest_framework import generics, viewsets
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.decorators import api_view
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from django.core import serializers
import json
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def about(request):
    return render(request, 'about.html')

def MenuItemsView(request):
    items = Menu.objects.all()
    return render(request, 'menu.html', {"menu": items})
#    queryset = Menu.objects.all()
#    serializer_class = MenuSerializer

def SingleMenuItemView(request, pk):
    item = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu_item.html', {'item': item})
#    queryset = Menu.objects.all()
#   serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

@csrf_exempt
def bookings(request):
    if request.method == "POST":
        data = json.loads(request.body)  # safer than json.load(request)
        #if not Booking.objects.filter(booking_date=data['booking_date']).exists():
        booking = Booking(
            name=data['name'],
            booking_date=data['booking_date'],
            no_of_guests=data['no_of_guests'],
        )
        booking.save()
        #else:
            #return HttpResponse("{'error':1}", content_type='application/json')
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.filter(booking_date=date)
    booking_json = serializers.serialize('json', bookings)
    return HttpResponse(booking_json, content_type='application/json')
        