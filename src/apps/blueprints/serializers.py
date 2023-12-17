from rest_framework.serializers import Serializer

from .models import Blueprint


class BlueprintSerializer(Serializer):

    class Meta:
        model = Blueprint
        fields = '__all__'
