from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('sightings/', views.sightings, name='Sightings'),
    path('sightings/add', views.sightings_add, name='add'),
    path('sightings/stats', views.sightings_stats, name = 'Some_Stats'),
    path('sightings/<str:Unique_Squirrel_ID>', views.update_squirrel, name='Update'),
    path('map/', views.map, name='map'),]

