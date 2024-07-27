from django.db import models
from django.contrib.auth.models import User

# Profile model with data fields for bio and profile_picture
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)

    def __str__(self):
        return self.user.username

# Project model with data fields for title, description, creation_date, due_date, state, owner, and is_public
class Project(models.Model):
    DRAFT = 'D'
    ONGOING = 'O'
    COMPLETED = 'C'
    CANCELLED = 'X'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (ONGOING, 'Ongoing'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    state = models.CharField(max_length=1, choices=STATUS_CHOICES, default=DRAFT)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def get_state_display(self):
        return dict(self.STATUS_CHOICES)[self.state]

# Task model with data fields for title, description, due_date, status, and project
class Task(models.Model):
    TODO = 'T'
    IN_PROGRESS = 'I'
    DONE = 'D'
    STATUS_CHOICES = [
        (TODO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=TODO)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title

# Comment model with data fields for user, project, task, content, and created_at
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username}"