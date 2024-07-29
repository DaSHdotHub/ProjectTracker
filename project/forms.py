from django import forms
from django.forms import inlineformset_factory
from .models import Project, Task

class ProjectForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'text', 'class': 'form-control', 'id': 'id_due_date'}
        )
    )

    class Meta:
        model = Project
        fields = ['title', 'description', 'due_date', 'state', 'is_public']
    
    # Override the __init__ method to limit the 'state' field choices
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['state'].choices = [
            (Project.DRAFT, 'Draft'),
            (Project.IN_PROGRESS, 'In Progress')        ]
        
class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'text', 'class': 'form-control', 'id': 'id_task_due_date'}
        )
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']        
