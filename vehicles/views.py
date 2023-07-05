from django.shortcuts import render
from utils.vehicles.factory import make_vehicle


def home(request):
    return render(request, 'vehicles/pages/home.html', context={
        'vehicles': [make_vehicle() for _ in range(9)],
    })


def vehicle(request, id):
    return render(request, 'vehicles/pages/vehicle_view.html', context={
        'vehicle': make_vehicle(),
        'is_detail_page': True,
    })
