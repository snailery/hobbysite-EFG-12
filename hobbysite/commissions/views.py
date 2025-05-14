from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Commission, Job, JobApplication
from .forms import CommissionForm, FullCommissionForm, JobFormSet, JobApplicationFormSet, ApplyToJobForm
from django.shortcuts import render, redirect, get_object_or_404


class CommissionListView(ListView):
    model = Commission
    template_name = 'commissions.html'


class CommissionDetailView(DetailView):
    model = Commission
    template_name = 'commission.html'


def commission_create(request):
    if (request.method == "POST"):
        commission_form = CommissionForm(request.POST)
        jobs_formset = JobFormSet(request.POST)

        if commission_form.is_valid() and jobs_formset.is_valid():
            commission = commission_form.save()
            jobs_formset.instance = commission
            jobs_formset.save()
            return redirect('commissions:commission', pk=commission.pk)
    else:
        commission_form = CommissionForm()
        jobs_formset = JobFormSet()

    ctx = {
        "commission_form": commission_form,
        "jobs_formset": jobs_formset
    }
    return render(request, "commission_create.html", ctx)


def commission_update(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    if (request.method == "POST"):
        # Check and Update Job Statuses
        for job in commission.jobs.filter(status="OPEN"):
            if (job.job_applications.filter(status="ACCEPTED").count() >= job.manpower_required):
                job.status = "FULL"
                job.save()

        # Check Commission Status
        if (commission.status != "FULL"):
            is_commission_full = True

        if (is_commission_full):
            commission_form = FullCommissionForm(request.POST, instance=commission)
        else:
            commission_form = CommissionForm(request.POST, instance=commission)
        jobs_formset = JobFormSet(request.POST, instance=commission)

        if commission_form.is_valid() and jobs_formset.is_valid():
            commission = commission_form.save()
            jobs_formset.save()

            # Update Commission Status
            if (is_commission_full):
                commission.status = "FULL"
                commission.save()
            return redirect('commissions:commission', pk=commission.pk)
    else:
        if (is_commission_full):
            commission_form = FullCommissionForm(instance=commission)
        else:
            commission_form = CommissionForm(instance=commission)
        jobs_formset = JobFormSet(instance=commission)

    ctx = {
        "commission_form": commission_form,
        "jobs_formset": jobs_formset
    }
    return render(request, "commission_update.html", ctx)
