from django.shortcuts import render

from squirrels.models import Squirrel

# Create your views here.

def map(request, *args, **kwargs):
    sightings = Squirrel.objects.all()[:70]
	context={
        'sightings':sightings
	}
	return render(request, 'map/map.html',context)
