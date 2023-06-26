from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html',
                  context={'name': 'Rafael Passos'},
                  )


def contato(request):
    return render(request, 'recipes/contato.html',
                  context={'name': 'Rafael Passos'}
                  )


def sobre(request):
    return HttpResponse('sobre')
