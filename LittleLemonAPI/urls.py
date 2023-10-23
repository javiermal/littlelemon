from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import SingleMenuItemView, MenuItemsView

urlpatterns = [
    path('menu-items', MenuItemsView.as_view()),
	path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
]