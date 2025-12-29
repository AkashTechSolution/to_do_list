from django.test import TestCase
import pytest
from django.db import connection
from tasks.db import init_db

# Create your tests here.
import json
from django.test import Client

@pytest.mark.django_db
def test_create_task():
    client = Client()
    response = client.post(
        "/api/tasks/create/",
        data=json.dumps({
            "title": "Test Task",
            "description": "Testing",
            "due_date": "2025-12-31",
            "status": "Pending"
        }),
        content_type="application/json"
    )
    assert response.status_code == 201


@pytest.mark.django_db
def test_get_tasks():
    client = Client()
    response = client.get("/api/tasks/")
    assert response.status_code == 200

@pytest.fixture(autouse=True)
def setup_db(db):
    """
    Automatically create tasks table
    before each test using raw SQL.
    """
    init_db()

def test_create_task_missing_title(client):
    response = client.post(
        "/api/tasks/create/",
        data='{}',
        content_type="application/json"
    )

    assert response.status_code == 400
    assert "Title is required" in response.json()["error"]

