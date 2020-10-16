from django.urls import path
from . import views

app = 'map'
urlpatterns = [
        path('map/', views.map, name='map'),]
