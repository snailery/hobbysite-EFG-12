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
            jobs_formset = JobFormSet(request.POST, instance=commission)

            if jobs_formset.is_valid():
                jobs = jobs_formset.save()
                return redirect('commission', pk=commission.pk)  # TODO pk, but might be id
        else:
            jobs_formset = JobFormSet(request.POST)  # TODO unsure

    ctx = {
        "commission": commission,
        "jobs": jobs,
        "commission_form": commission_form,
        "jobs_formset": jobs_formset
    }
    return render(request, "commission_create.html", ctx)


def commission_update(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    commission_form = CommissionForm(instance=commission)
    jobs_formset = JobFormSet(instance=commission)

    if (request.method == "POST"):
        jobs_formset = JobFormSet(request.POST, instance=commission)
        if jobs_formset.is_valid():
            if jobs_formset.cleaned_data:
                jobs = jobs_formset.save()
                return redirect('commission-edit', pk=commission.pk)
        else:
            commission_form = CommissionForm(instance=commission)
            ctx = {
                "commission": commission,
                "jobs": jobs,
                "commission_form": commission_form,
                "jobs_formset": jobs_formset
            }
            return render(request, "commission_update.html", ctx)

        commission_form = CommissionForm(request.POST, instance=commission)
        if commission_form.is_valid():
            commission = commission_form.save()
        else:
            jobs_formset = JobFormSet(request.POST)
            ctx = {
                "commission": commission,
                "jobs": jobs,
                "commission_form": commission_form,
                "jobs_formset": jobs_formset
            }
            return render(request, "commission_update.html", ctx)

    ctx = {
        "commission": commission,
        "jobs": jobs,
        "commission_form": commission_form,
        "jobs_formset": jobs_formset
    }
    return render(request, "commission_update.html", ctx)
