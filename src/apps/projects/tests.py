from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from apps.users.models import CustomUser
from apps.projects.models import Project


class ProjectTests(APITestCase):
    """
    router.register(r'projects', ProjectViewSet)
    router.register(r'project_notes', ProjectNotesViewSet)
    """

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create_user(
            username="test_user", password="test_password"
        )

        cls.project = Project.objects.create(
            title="Test Project", description="Test Project Description", user=cls.user
        )

    def test_projects_unauthenticated_cant_view(self):
        url = reverse("projects-list")
        response = self.client.get(url)

        self.assertNotEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

    def test_project_authenticated_can_view(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("projects-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_projects_only_owner_can_view(self):
        second_user = CustomUser.objects.create_user(
            username="second_user", email="second@user.com", password="second_password"
        )
        self.client.force_authenticate(user=second_user)
        url = reverse("projects-list")
        response = self.client.get(url)

        self.assertNotEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)
