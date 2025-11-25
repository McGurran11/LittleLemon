from django.contrib.auth.models import User
from .models import MenuItem
from rest_framework import serializers
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['title', 'price', 'inventory']