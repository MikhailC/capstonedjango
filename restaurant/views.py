from django.shortcuts import render
import django.views
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework.views import APIView

from restaurant import serializers
from restaurant.models import Menu, Booking
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.
def index(request):
    return render(request, 'index1.html', {})


class MenuItemView(ListCreateAPIView):
    serializer_class = serializers.MenuSerializer
    queryset = Menu.objects.all()


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    serializer_class = serializers.MenuSerializer
    queryset = Menu.objects.all()


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializer
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]


class HelloView(APIView):
   # permissions_classes = [IsAuthenticated]  # <-------- Only authenticated users can access this view

    def get(self, request):
        context = {"message": "Hello, World!"}  # <------ Response to the client
        return Response(context)
