from django.shortcuts import render, redirect
from .forms import ExtendedUserCreationForm
from django.contrib.auth.models import User
from profile.models import Profile


def register(request):
    if request.method == "POST":
        register_form = ExtendedUserCreationForm(request.POST)

        if register_form.is_valid():
            user = register_form.save()
            profile = Profile()
            profile.user = user
            profile.display_name = user.username
            return redirect("/accounts/login")
    else:
        register_form = ExtendedUserCreationForm()
    ctx = {}
    return render(request, 'registration/register.html', ctx)
