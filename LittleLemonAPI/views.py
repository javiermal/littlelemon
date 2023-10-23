from django.shortcuts import render
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
# Create your views here.

class MenuItemsView(ListCreateAPIView):
	queryset = MenuItem.objects.all()
	serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer