from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import profile, delete_account, ProfileViewSet

"""
DefaultRouter for Profile, Project, Task, and Comment ViewSets
"""

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)

urlpatterns = [
    path("", profile, name="profile"),
    path("delete-account/", delete_account, name="delete_account"),
    path("api/", include(router.urls)),
]
