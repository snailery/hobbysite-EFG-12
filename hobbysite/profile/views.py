from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile


def passport(request, username):
    user = User.objects.get(username=username)
    ctx = {
        'user': user,
        'profile': user.profile
    }
    return render(request, 'passport.html', ctx)
