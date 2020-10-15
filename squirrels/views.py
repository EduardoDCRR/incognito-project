from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Squirrel
#from .form import SForm


def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def sightings(request):
    all_squirrels = Squirrel.objects.all()
    data = ['Unique_Squirrel_ID','Date','X','Y']
    context = {
            'Squirrels': all_squirrels,
            'fields':data,
    }
    return render(request, 'squirrels/sightings.html',context)

def update_squirrel(request, Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
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
            return JsonResponse({'errors':form.errors},status=400)
    
    return JsonResponse({})

def sightings_stats(request):

    running_count = Squirrel.objects.values('Running').order_by('Running').annotate(run_count=Count('Running'))
    chasing_count = Squirrel.objects.values('Chasing').order_by('Chasing').annotate(run_count=Count('Chasing'))
    climbing_count = Squirrel.objects.values('Climbing').order_by('Climbing').annotate(run_count=Count('Climbing'))
    approaches_count = Squirrel.objects.values('Approaches').order_by('Approaches').annotate(run_count=Count('Approaches'))
    foraging_count = Squirrel.objects.values('Foraging').order_by('Foraging').annotate(run_count=Count('Foraging'))

    context = {
        'Running': running_count,
        'Chasing': chasing_count,
        'Climbing': climbing_count,
        'Approaches': approaches_count,
        'Foraging': foraging_count,
    }

    return render(request,'squirrels/stats.html',context)
