from django import forms
from .models import Profile


class ProfileDisplayNameForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name']
