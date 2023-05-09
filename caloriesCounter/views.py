from django.shortcuts import render, redirect
from .forms import CaloriesCounterForm
from .models import *

# Create your views here.


def index(request):
    total = 0
    data = CaloriesCounter.objects.all()
    for i in data:

        total += int(i.calories)
    return render(request, 'index.html', {'data': data, 'total': total})


def addCaloriesCounter(request):
    form = CaloriesCounterForm()
    if request.method == 'POST':
        form = CaloriesCounterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}

    # data = CaloriesCounterForm()
    return render(request, 'addfood.html', context)


def editCaloriesCounter(request, id):
    food = CaloriesCounter.objects.get(id=id)
    form = CaloriesCounterForm(instance=food)
    if request.method == 'POST':
        form = CaloriesCounterForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'edit.html', {'form': form})


def deleteCaloriesCounter(request, id):
    food = CaloriesCounter.objects.get(id=id)
    if request.method == 'POST':
        food.delete()

        return redirect('/')

    return render(request, 'delete.html', {'food': food})
