from django.urls import path


from . import views

urlpatterns = [
    path('', views.home),
    path('vehicles/<int:id>/', views.vehicles),



]
