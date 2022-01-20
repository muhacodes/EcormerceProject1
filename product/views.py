from django.shortcuts import render
from .models import Product
from backend.models import Testimonials
# Create your views here.


def HomeView(request):

    context = {
        'Testimonials' : Testimonials.objects.all()
    }

    return render(request, 'frontend/index.html', context)