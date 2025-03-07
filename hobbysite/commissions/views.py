from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Commission


class CommissionListView(ListView):
    model = Commission
    template_name = 'commissions.html'


class CommissionDetailView(DetailView):
    model = Commission
    template_name = 'commission.html'
