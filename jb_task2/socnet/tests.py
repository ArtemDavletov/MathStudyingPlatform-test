# import json
#
# from django.test import TestCase, Client
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIRequestFactory
#
# from jb_task2.socnet.models import User
#
# factory = APIRequestFactory()
# client = Client()
#
#
# # Create your tests here.
# class UserTestCase(TestCase):
#     def test_user_create(self):
#         data = {
#             'login': 'test',
#             'email': 'test@mail.ru'
#         }
#
#         response = client.post(
#             reverse('user_detail'),
#             data=json.dumps(data),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         assert User.objects.filter(login='test') is not None
