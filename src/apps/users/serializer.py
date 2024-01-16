from rest_framework.serializers import Serializer


from apps.users.models import CustomUser

class UserSerializer(Serializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class ProfileSerializer(Serializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
