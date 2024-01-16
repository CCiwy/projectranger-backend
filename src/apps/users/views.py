from django.shortcuts import render

from rest_framework.auth import isAuthenticated
from rest_framework import ModelViewset

from rest_framework import ModelViewset

from apps.users.serializer import UserSerializer
from apps.users.permissions import isSameUser

class UserView(ModelViewset):
    """ 
        permissions:
            get-detail: is_authenticated
            other: obj.id == request.user.id
    """
    serializer_class = UserSerializer
    queryset = Users.objects.all()


    def get_permissions(self, request):
        if self.action == 'retrieve':
            return [isAuthenticated]

        return [isSameUser]


        
