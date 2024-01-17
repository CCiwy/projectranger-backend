from rest_framework.test import APITestCase

from django.urls import reverse


class ProjectTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        self.project = Project.objects.create(title='Test Project', description='This is a test project')

    def test_get_projects(self):
        url = reverse('project-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

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
