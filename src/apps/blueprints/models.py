from django.db import models
from apps.languages.models import Language


class Blueprint(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class BlueprintLanguageWeight(models.Model):
    """ Weigth for Blueprint and Language """
    blueprint = models.ForeignKey(Blueprint, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=6, decimal_places=6)



