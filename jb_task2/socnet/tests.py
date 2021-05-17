import json

from django.test import TestCase, Client
from rest_framework import status

from jb_task2.socnet.models import User

client = Client()

URL = 'http://127.0.0.1:8000/api/'


# Create your tests here.
class UserTestCase(TestCase):
    def create_user(self, login='test', email='test@mail.ru'):
        data = {
            'login': login,
            'email': email
        }

        response = client.post(
            URL + 'user/',
            data=json.dumps(data),
            content_type='application/json'
        )

        return response

    def test_user_create(self):
        response = self.create_user()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert User.objects.filter(login='test') is not None

    def test_get_user(self):
        self.create_user()

        response = client.get(path=URL + 'user/test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_users(self):
        response = client.get(
            URL + 'all_users/',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_relationships(self):
        response = client.get(
            URL + 'all_relationships/',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_relationship(self):
        self.create_user(login='test1')
        self.create_user(login='test2')

        data = {
            "user_login": "test1",
            "friend_login": "test2"
        }

        response = client.post(
            URL + 'relationship/',
            data=json.dumps(data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_relationship(self):
        self.create_user(login='test1')
        self.create_user(login='test2')

        data = {
            "user_login": "test1",
            "friend_login": "test2"
        }

        client.post(
            URL + 'relationship/',
            data=json.dumps(data),
            content_type='application/json'
        )

        response = client.delete(path=URL + 'relationship/test1&test2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

