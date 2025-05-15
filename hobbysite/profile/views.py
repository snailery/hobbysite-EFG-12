from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile


def passport(request, username):
    user = get_object_or_404(User, username=username)
    ctx = {
        'user': user,
        'profile': user.profile
    }
    return render(request, 'passport.html', ctx)
