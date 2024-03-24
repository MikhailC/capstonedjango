from django.shortcuts import render
import django.views
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, DestroyAPIView

from restaurant import serializers
from restaurant.models import Menu, Booking


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
