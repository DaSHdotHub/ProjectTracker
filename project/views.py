from rest_framework import viewsets
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .forms import ProjectForm, TaskForm
from .models import Project, Task, Comment
from profiles.models import Profile
from .serializers import ProjectSerializer, TaskSerializer, CommentSerializer


# ViewSets
class BaseViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return self.queryset.all()


class ProjectViewSet(BaseViewSet):
    queryset = Project.objects
    serializer_class = ProjectSerializer


class TaskViewSet(BaseViewSet):
    queryset = Task.objects
    serializer_class = TaskSerializer


class CommentViewSet(BaseViewSet):
    queryset = Comment.objects
    serializer_class = CommentSerializer


# Helper functions
def get_user_profile(user):
    profile, _ = Profile.objects.get_or_create(user=user)
    return profile, profile.profile_picture


def get_common_context(request):
    user = request.user
    profile, profile_picture = get_user_profile(user)
    return {
        "user": user,
        "profile": profile,
        "profile_picture_url": profile_picture,
        "dashboard_url": reverse("dashboard"),
        "signout_url": reverse("signout"),
    }


# View for Dashboard (project list)
@login_required
def dashboard(request):
    projects = Project.objects.filter(owner=request.user)
    context = get_common_context(request)
    context.update(
        {
            "projects": projects,
            "comments": [
                {"user": "User 1", "content": "Comment content 1"},
                {"user": "User 2", "content": "Comment content 2"},
            ],
            "in_progress_count": projects.filter(state=Project.IN_PROGRESS).count(),
            "drafts_count": projects.filter(state=Project.DRAFT).count(),
            "total_count": projects.count(),
        }
    )
    return render(request, "project/project_list.html", context)

# View for Dashboard (project create)
@login_required
def create_project(request):
    context = get_common_context(request)
    if request.method == "POST":
        form = ProjectForm(request.POST, edit_mode=False)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect("dashboard")
    else:
        form = ProjectForm()
    context["form"] = form
    return render(request, "project/project_create.html", context)


@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    tasks = project.tasks.all()
    context = get_common_context(request)

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "project_edit":
            form = ProjectForm(request.POST, instance=project, edit_mode=True)
            if form.is_valid():
                form.save()
                messages.success(request, "Project updated successfully.")
                return redirect("project_edit", project_id=project.id)
            messages.error(request, "There was an error updating the project.")
        elif action == "add_task":
            task_form = TaskForm(request.POST)
            if task_form.is_valid():
                new_task = task_form.save(commit=False)
                new_task.project = project
                new_task.save()
                messages.success(request, "Task added successfully.")
                return redirect("project_edit", project_id=project.id)
            messages.error(request, "There was an error adding the task.")
    else:
        form = ProjectForm(instance=project, edit_mode=True)
        task_form = TaskForm()

    context.update(
        {
            "project": project,
            "form": form,
            "task_form": task_form,
            "tasks": tasks,
            "is_owner": request.user == project.owner,
            "has_tasks": tasks.exists(),
        }
    )
    return render(request, "project/project_edit.html", context)


@login_required
@csrf_exempt
def change_task_status(request):
    if request.method == "POST":
        task = get_object_or_404(
            Task, id=request.POST.get("task_id"), project__owner=request.user
        )
        task.status = request.POST.get("new_status")
        task.save()
        return JsonResponse({"success": True})


@login_required
@csrf_exempt
def delete_task(request):
    if request.method == "POST":
        task = get_object_or_404(
            Task, id=request.POST.get("task_id"), project__owner=request.user
        )
        task.delete()
        return JsonResponse({"success": True})
