from decimal import Decimal
from rest_framework import viewsets

from .serializers import ProjectSerializer
from .models import Project, ProjectNotes

class ProjectViewSet(viewsets.ModelViewSet):
    """ todo: add logic to return different serializers depending on ownersship """
    
    queryset = Project.objects.all()

    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):

        return ProjectSerializer


class ProjectNotesViewSet(viewsets.ModelViewSet):

    queryset = ProjectNotes.objects.all()

    def get_queryset(self):
        return ProjectNotes.objects.filter(project=self.kwargs['project_id'])




















