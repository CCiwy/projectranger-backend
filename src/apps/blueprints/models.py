from django.db import models

class ProjectBlueprint(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class BlueprintLanguageWeight(models.Model):
    blueprint = models.ForeignKey(ProjectBlueprint) # todo: cascaade on delete
    language = models.ForeignKey('languages.Language')
    weight = models.DecimalField(max_digits=6, decimal_places=6)



