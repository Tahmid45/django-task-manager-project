from django.shortcuts import render
from task_model.models import Task
# Create your views here.
def home(request):
    data = Task.objects.all()
    print(data)
    for i in data:
        print(i)
    return render(request, 'home.html', {'data':data})