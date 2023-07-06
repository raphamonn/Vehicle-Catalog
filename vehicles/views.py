from django.shortcuts import render, get_list_or_404, get_object_or_404
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
    vehicles = get_list_or_404(
        Vehicle.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id'))

    return render(request, 'vehicles/pages/category.html', context={
        'vehicles': vehicles,
        'title': f'{vehicles[0].category.name}'
    })


def vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, pk=id, is_published=True)

    return render(request, 'vehicles/pages/vehicle_view.html', context={
        'vehicle': vehicle,
        'is_detail_page': True,
    })
