from rest_framework.routers import DefaultRouter


from .views import BlueprintViewSet

router = DefaultRouter()
router.register(r'', BlueprintViewSet)


urlpatterns = router.urls
