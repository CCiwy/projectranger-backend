from rest_framework import serializers

from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    project_notes = serialiers.SerializerMethodField()


    class Meta:
        model = Project
        fields = '__all__'
        # fields = ('id', 'title', 'description', 'is_done', 'is_public', 'created_at', 'updated_at', 'github_url')


    def get_project_notes(self, obj):
        return ProjectNotesSerializer(obj.project_notes.all(), many=True).data

class ProjectNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'



class ProjectIdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        # fields = ('id', 'title', 'description', 'is_done', 'is_public', 'created_at', 'updated_at', 'github_url')


