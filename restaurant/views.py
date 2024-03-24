from django.shortcuts import render
import django.views

# Create your views here.
def index(request):
    return render(request, 'index1.html', {})
