from django.shortcuts import render
from utils.recipes.factory import make_recipe


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'vehicles': [make_recipe() for _ in range(10)],
    })


def vehicle(request, id):
    return render(request, 'recipes/pages/vehicle_view.html', context={
        'vehicle': make_recipe(),
    })
