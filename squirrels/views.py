from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Squirrel
from .forms import SForm
from django.db.models import Count


def sightings(request):

    data = ['Unique_Squirrel_ID','Date','X','Y']

    for row in Squirrel.objects.all().reverse():
        if Squirrel.objects.filter(Unique_Squirrel_ID=row.Unique_Squirrel_ID).count() > 1:
            row.delete()

    all_squirrels = Squirrel.objects.all()

    context = {
            'Squirrels': all_squirrels,
            'fields':data,
    }
    return render(request, 'squirrels/sightings.html',context)

def update_squirrel(request, Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)

    context = {
            'squirrel': squirrel,
    }
    if request.method == 'POST':
        form = SForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'squirrels/{Unique_Squirrel_ID}')
    else:
        form = SForm(instance=squirrel)

    context = {
        'form':form,
    }

    return render(request,'squirrels/update.html',context)



def sightings_add(request):
    if request.method == 'POST':
        form = SForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({}) 
    else:
        form = SForm()

    context = {
        'form': form,
    }

    return render(request, 'squirrels/add.html', context)

def sightings_stats(request):

    running_count = Squirrel.objects.values('Running').order_by('Running').annotate(running_count=Count('Running'))
    chasing_count = Squirrel.objects.values('Chasing').order_by('Chasing').annotate(chasing_count=Count('Chasing'))
    climbing_count = Squirrel.objects.values('Climbing').order_by('Climbing').annotate(climbing_count=Count('Climbing'))
    approaches_count = Squirrel.objects.values('Approaches').order_by('Approaches').annotate(approaches_count=Count('Approaches'))
    foraging_count = Squirrel.objects.values('Foraging').order_by('Foraging').annotate(foraging_count=Count('Foraging'))
    running = running_count[2]['running_count']
    chasing = chasing_count[2]['chasing_count']
    climbing = climbing_count[2]['climbing_count']
    approaches = approaches_count[2]['approaches_count']
    foraging = foraging_count[2]['foraging_count']

    context = {
        'Running': running,
        'Chasing': chasing,
        'Climbing': climbing,
        'Approaches': approaches,
        'Foraging': foraging,
    }

    return render(request,'squirrels/stats.html',context)

def map(request, *args, **kwargs):
    sightings = Squirrel.objects.all()[:70]
    context={
            'sightings':sightings
            }
    return render(request, 'map/map.html',context)

