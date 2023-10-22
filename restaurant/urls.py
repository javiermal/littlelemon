#define URL route for index() 
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	#path('api/', include('restaurant.urls')),
	path('menu/', views.MenuItemsView.as_view()),
	path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
