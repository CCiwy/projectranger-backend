from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from apps.users.models import CustomUser

TEST_USER_NAME = "TEST USER"
TEST_USER_MAIL = "mail@test.com"


class UserPermissionTests(APITestCase):
    @classmethod
    def setUp(cls):
        cls.user = CustomUser(username=TEST_USER_NAME, email=TEST_USER_MAIL)

        cls.url = reverse("user-detail")

    def view_profile_not_logged_in_returns_status_403(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code == status.HTTP_STATUS_FORBIDDEN)


# Create your tests here.
