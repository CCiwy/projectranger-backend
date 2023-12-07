from rest_framework.views import ModelViewSet



class LanguageView(ModelViewSet):

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
