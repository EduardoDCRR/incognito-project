from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Squirrel
from .form import SForm

def sightings(request):
    all_squirrels = Squirrel.objects.all()
    data = ['Unique_Squirrel_ID','Date','X','Y']
    context = {
            'Squirrels': squirrels,
            'fields':fields,
    }
    return(render, 'squirrels/sightings.html',context)

def sightings_add(request):
    if request.method == 'POST':
        form = SForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'errors':form.errors},status400)
    
    return JsonResponse({})

 

 Create your views here.
