from django.shortcuts import render, redirect
from .forms import ProfileRegisterForm
from django.contrib.auth.models import User
from profile.models import Profile


def register(request):
    if request.method == "POST":
        register_form = ProfileRegisterForm(request.POST)

        if register_form.is_valid():
            username = register_form.cleaned_data["username"]
            password = register_form.cleaned_data["password2"]
            profile = register_form.save(commit=False)

            user = User()
            user.username = username
            user.set_password(password)
            user.email = profile.email
            user.save()

            profile.user = user
            profile.save()
            return redirect("/accounts/login")
    else:
        register_form = ProfileRegisterForm()
    ctx = {'register_form': register_form}
    return render(request, 'registration/register.html', ctx)
