from django import forms
from .models import Commission, Job, JobApplication
from django.forms import inlineformset_factory


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        exclude = []


class FullCommissionForm(CommissionForm):
    class Meta:
        model = Commission
        exclude = ["status"]


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ["status"]


JobFormSet = inlineformset_factory(Commission, Job, form=JobForm)


class UpdateJobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        exclude = ["Job", "Profile"]


class CreateJobApplicationForm(UpdateJobApplicationForm):
    class Meta:
        exclude = ["Job", "Profile", "status"]
