from django.shortcuts import render
from datetime import datetime
from .models import *


def index(request):
    brands = Brands.objects.all()
    cars = Cars.objects.all()

    context = {
        'brands': brands,
        'cars': cars,
        'current_year': datetime.now().year
    }
    return render(request, 'index.html', context)

def brandDetail(request, brands_id):
    brands = Brands.objects.get(id=brands_id)
    cars = Cars.objects.filter(brand_id=brands_id)

    context = {
        'brands': [brands],
        'cars': cars,
        'current_year': datetime.now().year
    }

    return render(request, 'index.html', context)

def carDetail(request, cars_id):
    car = Cars.objects.get(id=cars_id)

    context = {
        'car': car,
        'current_year': datetime.now().year
    }

    return render(request, 'cars.html', context)