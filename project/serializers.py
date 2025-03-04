from rest_framework import serializers
from .models import Project, Task, Comment


# *.Serializer class inhereting from ModelSerializer and has a Meta class with the model set to *. and the fields set to *.fields
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "creation_date",
            "due_date",
            "state",
            "owner",
            "is_public",
        ]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "due_date", "status", "project"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "user", "project", "task", "content", "created_at"]
