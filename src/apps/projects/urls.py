from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, ProjectNotesViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'project_notes', ProjectNotesViewSet)

urlpatterns = router.urls
