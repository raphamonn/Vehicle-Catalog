from django.shortcuts import render
from utils.vehicles.factory import make_vehicle
from vehicles.models import Vehicle


def home(request):
    vehicles = Vehicle.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'vehicles/pages/home.html', context={
        'vehicles': vehicles
    })


def category(request, category_id):
    vehicles = Vehicle.objects.filter(
        category__id=category_id,
        is_published=True
    ).order_by('-id')
    return render(request, 'vehicles/pages/category.html', context={
        'vehicles': vehicles
    })


def vehicle(request, id):
    return render(request, 'vehicles/pages/vehicle_view.html', context={
        'vehicle': make_vehicle(),
        'is_detail_page': True,
    })
