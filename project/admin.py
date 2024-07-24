from django.contrib import admin
from .models import Profile, Project, Task, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Comment)