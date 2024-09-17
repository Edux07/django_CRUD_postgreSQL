from django.shortcuts import render, redirect
from .models import Task


def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'list_task.html',{'tasks': tasks})


def create_task(request):
    task = Task(title=request.POST['title'], descripcion=request.POST['description'])
    task.save()
    return redirect('/tasks/')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')
