from django import forms
from .models import Commission, Job, JobApplication
from django.forms import inlineformset_factory, modelformset_factory, BaseModelFormSet
from django.core.exceptions import ValidationError

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
        self.fields["job"].disabled = True


class BaseJobApplicationFormSet(BaseModelFormSet):
    def clean(self):
        # For each job, the no. of accepted applications should not exceed the manpower required
        if any(self.errors):
            return
        num_accepted = {}  # { job : no. of accepted applications}
        for form in self.forms:
            if self.can_delete and self._should_delete_form(form):
                continue

            job = form.cleaned_data.get("job")
            status = form.cleaned_data.get("status")

            if status == "B":  # Accepted
                num_accepted[job] = num_accepted.get(job, 0) + 1

        for job, count in num_accepted.items():
            if count > job.manpower_required:
                raise ValidationError("Too many accepted applications")


JobApplicationFormSet = modelformset_factory(
    JobApplication,
    form=JobApplicationForm,
    formset=BaseJobApplicationFormSet,
    edit_only=True,
    extra=0
)


class ApplyToJobForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        exclude = ["status", "Profile", "job"]
