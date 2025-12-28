from django.test import TestCase

# Create your tests here.
import json
import pytest
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
