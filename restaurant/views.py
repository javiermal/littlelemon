from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
#from rest_framework.decorators import permission_classes
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

# Create your views here.
def index(request):
	return render(request, "index.html",{})

class BookingViewSet(ModelViewSet):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
	permission_classes = [IsAuthenticated]
	def get(self, request):
		item = Booking.objects.all()
		serializer = BookingSerializer(item, many= True)
		return Response(serializer.data) #Return JSON

#def post(self, request):
#	serializer = MenuSerializer(data= request.data)
#	if serializer.is_valid():
#		serializer.save()
#		return Response({"status":"success", "data": serializer.data})

class MenuItemsView(ListCreateAPIView):
	permission_classes = [IsAuthenticated]
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

#class UserViewSet(ModelViewSet):
#   queryset = User.objects.all()
#   serializer_class = UserSerializer
#   permission_classes = [permissions.IsAuthenticated] 

