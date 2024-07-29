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
    return render(request, "project/project_list.html", context)

@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('../dashboard/')
    else:
        form = ProjectForm()        
    return render(request, "project/project_create.html", {'form': form})

@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    tasks = project.tasks.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        task_form = TaskForm(request.POST)
        if 'save_project' in request.POST and form.is_valid():
            form.save()
            return redirect('edit_project', project_id=project.id)
        elif 'save_task' in request.POST and task_form.is_valid():
            new_task = task_form.save(commit=False)
            new_task.project = project
            new_task.save()
            return redirect('edit_project', project_id=project.id)
    else:
        form = ProjectForm(instance=project)
        task_form = TaskForm()
        
    context = {
        'project': project,
        'form': form,
        'task_form': task_form,
        'tasks': tasks,
        'is_owner': request.user == project.owner,
        'has_tasks': tasks.exists(),
    }
    return render(request, 'project/edit_project.html', context)
