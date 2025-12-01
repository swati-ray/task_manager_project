from django.test import TestCase
from django.contrib.auth import get_user_model
from tasks.models import Task

User = get_user_model()

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')
        self.task = Task.objects.create(title='T1', description='D', owner=self.user)

    def test_created_default(self):
        self.assertFalse(self.task.completed)
        self.assertIsNotNone(self.task.created_at)
        self.assertIsNotNone(self.task.updated_at)

    def test_str(self):
        self.assertIn('T1', str(self.task))
