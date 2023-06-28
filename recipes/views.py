from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html',
                  context={'name': 'Rafael Passos'},
                  )


def vehicles(request, id):
    return render(request, 'recipes/pages/vehicles.html',
                  context={'name': 'Rafael Passos'},
                  )
