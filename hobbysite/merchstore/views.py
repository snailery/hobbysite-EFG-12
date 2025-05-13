from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product

# Create your views here.
class ItemListView(ListView):
    model = Product
    template_name = 'items.html'


class ItemDetailView(DetailView):
    model = Product
    template_name = 'item.html'
