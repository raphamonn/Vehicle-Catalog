from django.urls import path


from . import views


app_name = 'vehicles'

urlpatterns = [
    path('', views.home, name='home'),
    path('vehicle/category/<int:category_id>/',
         views.category, name='category'),
    path('vehicle/<int:id>/', views.vehicle, name='vehicle'),

]
