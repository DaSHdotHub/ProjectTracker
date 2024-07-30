from django import forms
from .models import Project, Task


class ProjectForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "text", "class": "form-control", "id": "id_due_date"}
        )
    )

    class Meta:
        model = Project
        fields = ["title", "description", "due_date", "state", "is_public"]
        widgets = {
            "title": forms.TextInput(attrs={"maxlength": "255"}),
            "description": forms.Textarea(attrs={"maxlength": "2048"}),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) > 255:
            raise forms.ValidationError("Title must be 255 characters or fewer.")
        return title

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if len(description) > 2048:
            raise forms.ValidationError("Description must be 2048 characters or fewer.")
        return description

    # Override the __init__ method to limit the 'state' field choices
    def __init__(self, *args, **kwargs):
        edit_mode = kwargs.pop("edit_mode", False)
        super(ProjectForm, self).__init__(*args, **kwargs)
        if not edit_mode:
            self.fields["state"].choices = [
                (Project.DRAFT, "Draft"),
                (Project.IN_PROGRESS, "In Progress"),
            ]
        else:
            self.fields["state"].choices = Project.STATUS_CHOICES


class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "text", "class": "form-control", "id": "id_task_due_date"}
        )
    )

    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "status"]
