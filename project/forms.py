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
        
TaskFormSet = inlineformset_factory(Project, Task, fields=['title', 'description', 'due_date', 'status'], extra=1)

