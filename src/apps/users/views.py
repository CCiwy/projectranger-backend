from rest_framework.http import Response
from rest_framework.auth import isAuthenticated
from rest_framework import ModelViewset


from apps.users.serializer import UserSerializer, ProfileSerializer
from apps.users.models import Users, Profile, UserFriendShip
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




class ProfileView(ModelViewset):
    """ 
        permissions:
            get-detail: is_authenticated
            other: obj.id == request.user.id
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


    


    def add_friend(self, request):
        """ add a friend """
        friend_id = request.data.get('friend_id')
        friend = Users.objects.get(id=friend_id)
        # todo: use friendshiprequest serializer
        UserFriendShip(user=request.user, friend=friend)


        return Response({'message': 'friend added'})
