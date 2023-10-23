from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory
from restaurant.models import Menu  # Import your Menu model
from restaurant.serializers import MenuSerializer
from restaurant.views import MenuItemsView

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(title='Pizza', price=12.0, inventory=50)
        Menu.objects.create(title='Burger', price=15.0, inventory=20)
        # Add more test instances as needed

    def test_getall(self):
        factory = APIRequestFactory()
        view = MenuItemsView.as_view()

        # Create a GET request to retrieve all Menu items
        request = factory.get('/menu-items/')
        response = view(request)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Serialize the retrieved Menu items
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)