from rest_framework import viewsets
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .forms import ProjectForm, TaskForm
from .models import Project, Task, Comment
from .serializers import (
    ProjectSerializer,
    TaskSerializer,
    CommentSerializer,
)


# ViewSets for Project, Task, and Comment models
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@login_required
def dashboard(request):
    user = request.user
    projects = Project.objects.filter(owner=user)
    comments = [
        {"user": "User 1", "content": "Comment content 1"},
        {"user": "User 2", "content": "Comment content 2"},
    ]

    in_progress_count = projects.filter(state="in_progress").count()
    drafts_count = projects.filter(state="draft").count()
    total_count = projects.count()

    context = {
        "projects": projects,
        "comments": comments,  # TODO: Replace with actual comments
        "in_progress_count": in_progress_count,
        "drafts_count": drafts_count,
        "total_count": total_count
        
    }
    return render(request, "project/project_list.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, edit_mode=False)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect("dashboard")
    else:
        form = ProjectForm()
    
    context = {
        "form": form,
        "dashboard_url": reverse('dashboard'),
    }
    return render(request, "project/project_create.html", context)


@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    tasks = project.tasks.all()
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "edit_project":
            form = ProjectForm(request.POST, instance=project, edit_mode=True)
            if form.is_valid():
                form.save()
                messages.success(request, "Project updated successfully.")
                return redirect("edit_project", project_id=project.id)
            else:
                messages.error(request, "There was an error updating the project.")

        elif action == "add_task":
            task_form = TaskForm(request.POST)
            if task_form.is_valid():
                new_task = task_form.save(commit=False)
                new_task.project = project
                new_task.save()
                messages.success(request, "Task added successfully.")
                return redirect("edit_project", project_id=project.id)
            else:
                messages.error(request, "There was an error adding the task.")
    else:
        form = ProjectForm(instance=project, edit_mode=True)
        task_form = TaskForm()

    context = {
        "project": project,
        "form": form,
        "task_form": task_form,
        "tasks": tasks,
        "is_owner": request.user == project.owner,
        "has_tasks": tasks.exists(),
        "dashboard_url": reverse('dashboard'),
    }
    return render(request, "project/edit_project.html", context)


@login_required
@csrf_exempt
def change_task_status(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        new_status = request.POST.get("new_status")
        task = get_object_or_404(Task, id=task_id, project__owner=request.user)
        task.status = new_status
        task.save()
        return JsonResponse({"success": True})


@login_required
@csrf_exempt
def delete_task(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        task = get_object_or_404(Task, id=task_id, project__owner=request.user)
        task.delete()
        return JsonResponse({"success": True})
