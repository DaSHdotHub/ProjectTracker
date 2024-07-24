from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, ProjectViewSet, TaskViewSet, CommentViewSet

# DefaultRouter for Profile, Project, Task, and Comment ViewSets
router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]