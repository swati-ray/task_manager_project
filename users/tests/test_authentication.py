from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthTests(APITestCase):
    def test_register_and_login(self):
        url = reverse('user-register')
        data = {'username': 'john', 'email': 'john@example.com', 'password': 'StrongPass123!', 'password_confirm': 'StrongPass123!'}
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        login_url = reverse('token-obtain')
        resp2 = self.client.post(login_url, {'username': 'john', 'password': 'StrongPass123!'}, format='json')
        self.assertEqual(resp2.status_code, status.HTTP_200_OK)
        self.assertIn('access', resp2.data)
