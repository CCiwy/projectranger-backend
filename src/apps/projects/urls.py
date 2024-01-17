from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, ProjectNotesViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'project_notes', ProjectNotesViewSet, basename='notes')

urlpatterns = router.urls
