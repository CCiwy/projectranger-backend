from rest_framework import serializers


from .models import Blueprint


class BlueprintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blueprint
        fields = '__all__'
