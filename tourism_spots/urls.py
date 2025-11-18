from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('spots-data/', views.tourist_spots_data, name='tourist_spots_data'),
]