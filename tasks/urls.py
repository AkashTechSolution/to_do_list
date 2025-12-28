from django.urls import path
from . import views

urlpatterns = [
    # API
    path("api/tasks/create/", views.create_task),
    path("api/tasks/", views.get_tasks),

    # Templates
    path("", views.task_list_view, name="task_list"),
    path("add/", views.add_task_view, name="add_task"),
]
