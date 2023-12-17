from django.shortcuts import render
from rest_framework import viewsets

from apps.projects.models import Project

from apps.blueprints.models import Blueprint
from .serializers import BlueprintSerializer

class BlueprintViewSet(viewsets.ModelViewSet):


    def get_queryset(self):
        return Blueprint.objects.all()

    def get_serializer_class(self):
        return BlueprintSerializer


    def get_project_for_user(self):

        user = self.kwargs['user']

        start_date = self.kwargs.get('start_date', False)
        language = self.kwargs.get('language', False)
        q = Project.objects.filter(owner=user)
        if start_date:
            q = q.filter(created_at__gte=start_date) 
        if language:
            q = q.filter(projectlanguage__language=language)

        return q


    def calculate_threshold(self, skill_level, language_skill):
        """ Calculate the threshold for a project idea based on the skill level of the user and the skill level of the language
            both range from 0 to 1
        """
        return skill_level * language_skill




    def get_project_idea_full_by_language(self):
        general_skill = self.kwargs['general_skill'] # how good as a programmer are you?
        languages = self.kwargs['languages'] # what languages do you like or dislike or want to learn?
        # frameworks = self.kwargs['frameworks'] # what frameworks do you like or dislike or want to learn?
        tags = self.kwargs['tags'] # game, web, mobile, desktop, office, organize, etc.

        # some formula to calculate the best project idea for you
        # based on your skill level, your language preferences, and your framework preferences
        # and the weights of each language and framework for each project idea


        # calculate skill level -> threshold
        # calculate skill per language
        limit = 10 # todo: make this constant? parameter?

        result = []
        languages = Language.objects.filter(name__in=languages)
        for language in languages:
            threshold = calculate_threshold(Decimal(general_skill), Decimal(language_skill))
            ideas = LanguageProjects.objects.filter(language_in=languages, weight__lte=threshold).order_by('-weight')[:limit]
            result.extend(ideas)
        
        return result
