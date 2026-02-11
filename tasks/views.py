from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.http import JsonResponse

# Create your views here.

def task_list_view(request):
    task_items = Task.objects.all().values()
    return JsonResponse(list(task_items), safe=False)

def task_create_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        status = request.POST.get("status")
        Task.objects.create(title=title, description=description, status=status)
        return redirect("task_create_view")
    
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})

def task_update_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == "POST":
        task.title = request.POST.get('title')
        task.status = request.POST.get("status")
        task.description = request.POST.get("description")
        task.save()
        return redirect('task_create_view')
    return render(request, 'tasks/task_edit.html', {'task': task})