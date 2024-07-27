from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, TaskFormSet
from .models import Profile, Project, Task, Comment
from .serializers import ProfileSerializer, ProjectSerializer, TaskSerializer, CommentSerializer

# ViewSets for Profile, Project, Task, and Comment models
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

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
    
    in_progress_count = projects.filter(state='in_progress').count()
    drafts_count = projects.filter(state='draft').count()
    total_count = projects.count()
    
    context = {
        "projects": projects,
        "comments": comments,  # TODO: Replace with actual comments
        "in_progress_count": in_progress_count,
        "drafts_count": drafts_count,
        "total_count": total_count,
    }
    return render(request, "project/dashboard.html", context)

@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()        
    return render(request, "project/create_project.html", {'form': form})

@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        task_formset = TaskFormSet(request.POST, instance=project)
        if form.is_valid() and task_formset.is_valid():
            form.save()
            task_formset.save()
            return redirect('dashboard')
    else:
        form = ProjectForm(instance=project)
        task_formset = TaskFormSet(instance=project)
    return render(request, 'project/edit_project.html', {'form': form, 'task_formset': task_formset})