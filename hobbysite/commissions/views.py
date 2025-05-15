from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Commission, Job, JobApplication
from .forms import CommissionForm, FullCommissionForm, JobFormSet, JobApplicationFormSet, ApplyToJobForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.contrib.auth.decorators import login_required


class CommissionListView(ListView):
    model = Commission
    template_name = 'commissions/commissions.html'


def commission_detail(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    jobs = commission.jobs.all()
    job_applications = JobApplication.objects.filter(job__commission=commission)
    accepted_job_applications_count = job_applications.filter(status="B").count()
    total_manpower = commission.jobs.aggregate(Sum("manpower_required"))["manpower_required__sum"] or 0
    open_manpower = total_manpower - accepted_job_applications_count

    if request.method == "POST":
        job_id = request.POST.get('job_id')
        job = get_object_or_404(jobs, pk=job_id)
        apply_form = ApplyToJobForm(request.POST)

        if apply_form.is_valid():
            job_application = apply_form.save(commit=False)
            job_application.job = job
            job_application.applicant = request.user.profile
            job_application.save()
            return redirect("commissions:commission", pk=commission.pk)
    else:
        apply_form = ApplyToJobForm()

    ctx = {
        "commission": commission,
        "open_manpower": open_manpower,
        "total_manpower": total_manpower,
        "apply_form": apply_form
    }
    return render(request, "commissions/commission.html", ctx)


@login_required
def commission_create(request):
    if (request.method == "POST"):
        commission_form = CommissionForm(request.POST)
        jobs_formset = JobFormSet(request.POST)

        if commission_form.is_valid() and jobs_formset.is_valid():
            commission = commission_form.save(commit=False)
            commission.author = request.user.profile
            commission.save()
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
    return render(request, "commissions/commission_create.html", ctx)


@login_required
def commission_update(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    # Check Commission Status
    is_commission_full = True
    if (commission.jobs.filter(status="OPEN").exists()):
        is_commission_full = False

    if (request.method == "POST"):
        # Instantiate Forms
        if (is_commission_full):
            commission_form = FullCommissionForm(request.POST, instance=commission)
        else:
            commission_form = CommissionForm(request.POST, instance=commission)
        jobs_formset = JobFormSet(request.POST, instance=commission)
        job_application_formset = JobApplicationFormSet(request.POST, queryset=JobApplication.objects.filter(job__commission=commission))

        # Form Validation
        if commission_form.is_valid() and jobs_formset.is_valid() and job_application_formset.is_valid():
            commission = commission_form.save(commit=False)
            commission.author = request.user.profile
            commission.save()
            jobs_formset.save()
            job_application_formset.save()

            # Check and Update Job Statuses
            for job in commission.jobs.all():
                job.status = "OPEN"
                if (job.job_applications.filter(status="B").count() >= job.manpower_required):  # status "B" is "ACCEPTED"
                    job.status = "FULL"
                job.save()

            # Recheck Commission Status
            is_commission_full = True
            if (commission.jobs.filter(status="OPEN").exists()):
                is_commission_full = False

            # Update Commission Status
            if (is_commission_full):
                commission.status = "FULL"
            else:
                commission.status = "OPEN"
            commission.save()

            return redirect('commissions:commission', pk=commission.pk)
    else:
        if (is_commission_full):
            commission_form = FullCommissionForm(instance=commission)
        else:
            commission_form = CommissionForm(instance=commission)
        jobs_formset = JobFormSet(instance=commission)
        job_application_formset = JobApplicationFormSet(queryset=JobApplication.objects.filter(job__commission=commission))

    ctx = {
        "commission_form": commission_form,
        "jobs_formset": jobs_formset,
        "job_application_formset": job_application_formset
    }
    return render(request, "commissions/commission_update.html", ctx)
