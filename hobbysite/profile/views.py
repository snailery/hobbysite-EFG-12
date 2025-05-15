from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileDisplayNameForm


def passport(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile

    if request.method == 'POST':
        form = ProfileDisplayNameForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('passport', username=username)
    else:
        form = ProfileDisplayNameForm(instance=profile)

    ctx = {
        'user': user,
        'profile': profile,
        'form': form
    }
    return render(request, 'passport.html', ctx)
