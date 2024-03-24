from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/', views.MenuItemView.as_view()),
    path('item/<int:pk>/', views.SingleMenuItemView.as_view()),
]
