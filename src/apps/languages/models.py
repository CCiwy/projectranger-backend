from django.db import models


class Language(models.Model):
    """ Coding language model """
    name = models.CharField(max_length=24)
    description = models.TextField(max_length=255)
    paradigm = models.CharField(max_length=24)


