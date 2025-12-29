from django.shortcuts import render

# Create your views here.
import json
import logging
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

logger = logging.getLogger(__name__)

# ------------------------
# API ENDPOINTS
# ------------------------

@csrf_exempt
def create_task(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    try:
        data = json.loads(request.body)

        # Validation
        if not data.get("title"):
            return JsonResponse({"error": "Title is required"}, status=400)

        # Database operation
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO tasks (title, description, due_date, status)
                VALUES (%s, %s, %s, %s)
                """,
                [
                    data.get("title"),
                    data.get("description"),
                    data.get("due_date"),
                    data.get("status", "Pending"),
                ]
            )

        # Success log
        logger.info("Task created successfully")

        return JsonResponse({"message": "Task created"}, status=201)

    except Exception as e:
        # Error log
        logger.error(f"Database error: {e}")
        return JsonResponse({"error": "Internal server error"}, status=500)

def get_tasks(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, title, description, due_date, status FROM tasks")
        rows = cursor.fetchall()

    tasks = [
        {
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "due_date": row[3],
            "status": row[4],
        }
        for row in rows
    ]

    return JsonResponse(tasks, safe=False)


def task_list_view(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, title, description, due_date, status FROM tasks")
        tasks = cursor.fetchall()

    return render(request, "tasks/task_list.html", {"tasks": tasks})


def add_task_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")

        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO tasks (title, description, due_date, status)
                VALUES (%s, %s, %s, %s)
                """,
                [title, description, due_date, "Pending"]
            )

        return redirect("task_list")

    return render(request, "tasks/add_task.html")

