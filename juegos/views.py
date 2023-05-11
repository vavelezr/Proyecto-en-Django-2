from django.shortcuts import render
from .models import Juegos
# Create your views here.

def juegos(request):
    juegoss = Juegos.objects.all().order_by('-ano')
    return render(request, 'juegos.html', {'juegoss':juegoss})