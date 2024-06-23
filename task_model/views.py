from django.shortcuts import render, redirect
from .forms import TaskForm
from . import models
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        form  = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form  = TaskForm()
    return render(request, 'add_task.html', {'form':form})

def edit_task(request, id):
    task = models.Task.objects.get(pk=id)
    form = TaskForm(instance = task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        return render(request, 'add_task.html',{'form':form})

def complete_task(request, id):
    task = models.Task.objects.get(pk=id)
    task.is_completed = True
    return redirect('homepage')

def delete_task(request, id):
    task = models.Task.objects.get(pk=id)
    task.delete()
    return redirect('homepage')