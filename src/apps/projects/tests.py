from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from .apps.users.models import User
from .apps.projects.models import Project



class ProjectTests(APITestCase):
    """
    router.register(r'projects', ProjectViewSet)
    router.register(r'project_notes', ProjectNotesViewSet)
    """
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='test_user',
            password='test_password'
            )
        cls.project = Project.objects.create(
            name='Test Project',
            description='Test Project Description',
            owner=cls.user
        )


    def test_projects_unauthenticated_cant_view(self):
        url = reverse('projects-list')
        print(url)
        response = self.client.get(url)

        self.assertNotEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)
