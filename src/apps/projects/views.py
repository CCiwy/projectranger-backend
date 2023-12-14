from rest_framework import viewsets


class ProjectsViewset(viewsets.ModelViewSet):


    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):
        return ProjectSerializer


