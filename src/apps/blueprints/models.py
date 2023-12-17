from django.db import models

class Blueprint(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class BlueprintLanguageWeight(models.Model):
    blueprint = models.ForeignKey(Blueprint, on_delete=models.CASCADE)
    language = models.ForeignKey('languages.Language', on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=6, decimal_places=6)



