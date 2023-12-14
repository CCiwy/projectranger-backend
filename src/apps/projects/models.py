from django.db import models



class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    github_url = models.URLField(blank=True)


class ProjectNotes(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class ProjectIdea(models.Model):
    """ Ideas for projects: Title, description, and weights to languages and frameworks + skill levels,

    """

    title = models.CharField(max_length=100)
    description = models.TextField()


class ProjectLanguage(models.Model):
    projectIdea = models.ForeignKey(ProjectIdea, on_delete=models.CASCADE)
    language = models.ForeignKey('languages.Language', on_delete=models.CASCADE)

    weight = models.DecimalField(max_digits=6, decimal_places=6)


class ProjectSkill(models.Model):
    projectIdea = models.ForeignKey(ProjectIdea, on_delete=models.CASCADE)
    skill = models.ForeignKey('skills.Skill', on_delete=models.CASCADE) # todo: add skills app!

    weight = models.DecimalField(max_digits=6, decimal_places=6)
