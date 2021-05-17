from django.shortcuts import render
from .models import *

def Home(request):
    events = Event.objects.all().order_by('-date_published')

    return render(request, 'main/home.html', {'events': events})