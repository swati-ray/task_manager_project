from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from tasks.models import Task

User = get_user_model()

class TaskViewsTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass123')
        url = reverse('token-obtain')
        resp = self.client.post(url, {'username': 'tester', 'password': 'pass123'}, format='json')
        self.access = resp.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access}')

    def test_create_task(self):
        url = reverse('task-list')
        data = {'title': 'New', 'description': 'Desc', 'completed': False}
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

    def test_list_tasks_empty(self):
        url = reverse('task-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
