from django.shortcuts import render

from minerals.models import Mineral
import random


def index(request):
    """Landing 'home' page view to display list of all mineral names"""
    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    return render(request, 'index.html', {'minerals': minerals, 'random_mineral': random_mineral})
