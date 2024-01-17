from rest_framework.views import ModelViewSet

from .models import Language
from .serializers import LanguageSerializer



class LanguageView(ModelViewSet):

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
