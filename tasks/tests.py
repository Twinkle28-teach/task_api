from datetime import date, timedelta
from rest_framework.test import APITestCase
from .models import Task

# Create your tests here.
class TaskAPITests(APITestCase):
    def setUp(self):
        Task.objects.create(title="Task A",status = "DONE")
        Task.objects.create(title="Task B",status = "TODO")
        Task.objects.create(title="Task C",status = "TODO")

    def test_list_tasks(self):
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_filter_by_status(self):
        response = self.client.get("/api/tasks/?status=TODO")
        self.assertEqual(len(response.data), 2)

    def test_filter_is_case_insensitive(self):
        response = self.client.get("/api/tasks/?status=done")
        self.assertEqual(len(response.data), 1)

    def test_filter_unknown_status_returns_empty(self):
        response = self.client.get("/api/tasks/?status=xyz")
        self.assertEqual(len(response.data), 0)

    def test_create_task(self):
        data = {"title": "New task", "status": "TODO"}
        response = self.client.post("/api/tasks/", data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Task.objects.count(), 4)

    def test_past_due_date_rejected(self):
        yesterday = date.today()- timedelta(days=1)
        data = {"title":"Old task","due_date":str(yesterday)}
        response = self.client.post("/api/tasks/", data)
        self.assertEqual(response.status_code, 400)



        