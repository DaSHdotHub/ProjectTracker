from django import forms
from django.contrib.auth.models import User
from .models import Profile

"""
Form for updating the profile picture
"""


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_picture"]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields["profile_picture"].widget.attrs.update({"class": "form-control-file"})



"""
Form for updating the user details
"""


class UserForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(), required=False, label="New Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(), required=False, label="Confirm New Password"
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
