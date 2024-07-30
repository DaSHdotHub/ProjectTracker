from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    dashboard,
    public_dashboard,
    create_project,
    edit_project,
    change_task_status,
    delete_task,
    ProjectViewSet,
    TaskViewSet,
    CommentViewSet,
)

# DefaultRouter for Project, Task, and Comment ViewSets
router = DefaultRouter()
router.register(r"projects", ProjectViewSet)
router.register(r"tasks", TaskViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("public-dashboard/", public_dashboard, name="public_dashboard"),
    path("create-project/", create_project, name="create_project"),
    path("edit-project/<int:project_id>/", edit_project, name="edit_project"),
    path("change-task-status/", change_task_status, name="change_task_status"),
    path("delete-task/", delete_task, name="delete_task"),
    path("api/", include(router.urls)),
]
