from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Commission, Job, JobApplication
from .forms import CommissionForm, JobFormSet, CreateJobApplicationForm
from django.shortcuts import render, redirect, get_object_or_404


class CommissionListView(ListView):
    model = Commission
    template_name = 'commissions.html'


class CommissionDetailView(DetailView):
    model = Commission
    template_name = 'commission.html'


def commission_create(request):
    commission_form = CommissionForm()

    if (request.method == "POST"):
        commission_form = CommissionForm(request.POST)

        if commission_form.is_valid():
            commission = commission_form.save()
            commission_jobs = JobFormSet(request.POST, instance=commission)

            if commission_jobs.is_valid():
                commission_jobs.save()
                return redirect('commission', pk=commission.pk)  # TODO pk or id
        else:
            commission_jobs = JobFormSet(request.POST)  # TODO unsure

    ctx = {"commission": commission, "commission_jobs": commission_jobs}
    return render(request, "commission_create.html", ctx)
