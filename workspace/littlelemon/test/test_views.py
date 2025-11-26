from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = Menu.objects.create(title="Burger", price=50, inventory=200)

    def test_get_all_menu_items(self):
        response = self.client.get('/restaurant/menu/items/')
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
