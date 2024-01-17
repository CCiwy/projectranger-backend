from django.db import models


class Language(models.Model):
    """ Coding language model """
    name = models.CharField(max_length=24)
    description = models.TextField(max_length=255)
    paradigm = models.CharField(max_length=24)


class BlueprintLanguageWeight(models.Model):
    """ Weigth for Blueprint and Language """
    blueprint = models.ForeignKey('blueprints.Blueprint', on_delete=models.CASCADE)
    language = models.ForeignKey('languages.Language', on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=6, decimal_places=6)
