from django import forms
from .models import Commission, Job, JobApplication
from django.forms import inlineformset_factory


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = '__all__'


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ["status"]


JobFormSet = inlineformset_factory(Commission, Job, form=JobForm, extra=5)


class UpdateJobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        exclude = ["Job", "Profile"]


class CreateJobApplicationForm(UpdateJobApplicationForm):
    class Meta:
        exclude = ["Job", "Profile", "status"]
