from django.shortcuts import render

class Marker:
    def __init__(self, location):
        self.location = location

markers = [
    Marker('White Plains'),
    Marker('Lexington'),
    Marker('Concord'),
    Marker('Brooklyn'),
]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def marker_index(request):
    return render(request, 'markers/index.html', {'markers': markers})
