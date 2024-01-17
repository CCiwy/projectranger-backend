from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    github_url = models.URLField(blank=True)
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)


class ProjectEntity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProjectNotes(ProjectEntity):
    entity_type = "note"


class ProjectTodos(ProjectEntity):
    entity_type = "todo"


class ProjectIdea(ProjectEntity):
    entity_type = "idea"
