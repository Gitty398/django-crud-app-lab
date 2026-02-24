from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Marker


def marker_index(request):
    markers = Marker.objects.all()
    return render(request, 'markers/index.html', {'markers': markers})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def marker_detail(request, marker_id):
    marker = Marker.objects.get(id=marker_id)
    return render(request, 'markers/detail.html', {'marker': marker})
