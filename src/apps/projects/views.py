from decimal import Decimal
from rest_framework import viewsets

from .serializers import ProjectSerializer


class ProjectsViewset(viewsets.ModelViewSet):
    """ todo: add logic to return different serializers depending on ownersship """

    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):

        return ProjectSerializer


class ProjectNotesViewset(viewsets.ModelViewSet):


    def get_queryset(self):
        return ProjectNotes.objects.filter(project=self.kwargs['project_id'])




















