from django.db import models


class Language(Model):
    name = models.CharField(max_length=24)
    description = models.TextField(max_length=255)
    
