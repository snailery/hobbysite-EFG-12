from django import forms
from .models import Commission, Job, JobApplication
from django.forms import inlineformset_factory, modelformset_factory


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
        exclude = []
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields["Profile"].disabled = True
        self.fields["status"].disabled = True


JobFormSet = inlineformset_factory(Commission, Job, form=JobForm)


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields["Profile"].disabled = True
        self.fields["Job"].disabled = True
        

JobApplicationFormSet = modelformset_factory(
    JobApplication,
    form=JobApplicationForm,
    edit_only=True,
    extra=0
)


class ApplyToJobForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        exclude = ["Job", "Profile", "status"]
