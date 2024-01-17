from rest_framework.routers import DefaultRouter

from apps.users.views import UserView, ProfileView

router = DefaultRouter()

router.register('', UserView.as_view(), basename='user')
router.register('', ProfileView.as_view(), basename='profile')
router.register('add_friend', ProfileView.as_view({'post': 'add_friend'}), basename='add_friend')


urlpatterns = []
urlpatterns+= router.urls
