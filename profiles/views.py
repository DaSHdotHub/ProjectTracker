from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .serializers import ProfileSerializer
from .forms import ProfileForm, UserForm
from .utils import upload_profile_picture


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


"""
Profile page interaction
"""


@login_required
def profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile = profile_form.save(commit=False)
            profile_updated = False

            if "profile_picture" in request.FILES:
                profile_picture_url = upload_profile_picture(
                    request.FILES["profile_picture"]
                )
                profile.profile_picture = profile_picture_url

            profile.save()

            if user_form.cleaned_data.get("password1"):
                user.set_password(user_form.cleaned_data["password1"])
                user.save()
                update_session_auth_hash(request, user)

            messages.success(request, "Your profile was successfully updated!")
            # Set a session variable to flag that the profile was updated
            profile_updated = True
            request.session["profile_updated"] = True
            return redirect("profile")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    profile_picture_url = profile.profile_picture if profile.profile_picture else None

    # Check if the profile was updated in this session
    show_dashboard_button = request.session.get("profile_updated", False)

    return render(
        request,
        "profiles/profiles.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "profile_picture_url": profile_picture_url,
            "show_dashboard_button": show_dashboard_button,
        },
    )


"""
User deletion
"""


@login_required
def delete_account(request):
    user = request.user
    if request.method == "POST":
        user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect("home")
    return render(request, "profiles/delete_account.html")
