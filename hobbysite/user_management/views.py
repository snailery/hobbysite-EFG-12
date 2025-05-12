from django.shortcuts import render
from django.contrib.auth.models import User


def passport(request, username):
    ctx = {
        'user': User.objects.get(username=username),
    }
    return render(request, 'user_management/passport.html', ctx)
