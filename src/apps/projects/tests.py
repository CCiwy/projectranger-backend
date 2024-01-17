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
            username='test_user',
            password='test_password'
            )

        cls.project = Project.objects.create(
            title='Test Project',
            description='Test Project Description',
            user=cls.user
        )
 

    def test_projects_unauthenticated_cant_view(self):
        url = reverse('projects-list')
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)



"""

    def test_get_project_by_id(self):
        url = reverse('project-detail', kwargs={'pk': self.project.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)


    def test_create_project(self):
        url = reverse('project-list')
        data = {
            'title': 'Test Project 2',
            'description': 'This is also a test project'
        }


        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
"""
