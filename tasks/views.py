# Add all your views here

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from tasks.models import Task


def tasks_view(request):
    tasks_list = Task.objects.filter(deleted=False, completed=False)
    search_term = request.GET.get("search")

    if search_term:
        tasks_list = tasks_list.filter(
            deleted=False, completed=False, title=search_term
        )
    return render(request, "tasks.html", {"tasks_list": tasks_list})


def add_tasks(request):
    task = request.GET.get("task")
    Task(title=task).save()

    return HttpResponseRedirect("/tasks")


def delete_task(request, index):
    task = Task.objects.filter(id=index)
    task.update(deleted=True)

    return HttpResponseRedirect("/tasks")


def mark_as_done(request, index):
    task = Task.objects.filter(id=index)
    task.update(completed=True)

    return HttpResponseRedirect("/tasks")


def completed(request):
    completed_items = Task.objects.filter(completed=True)
    return render(request, "completed.html", {"completed": completed_items})
