from rest_framework.routers import DefaultRouter

from apps.users.views import UserView

router = DefaultRouter()

router.register('', UserView.as_view(), basename='user')


urlpatterns+= router.urls
