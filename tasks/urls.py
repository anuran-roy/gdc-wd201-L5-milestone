from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.tasks_view),
    path("add-task/", views.add_tasks),
    path("delete-task/<int:index>/", views.delete_task),
    path("complete_task/<int:index>/", views.mark_as_done),
    path("completed_tasks/", views.completed)
    # Add all your views here
]
