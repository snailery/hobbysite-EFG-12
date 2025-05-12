from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product


class ItemListView(ListView):
    model = Product
    template_name = 'merchstore/items.html'


class ItemDetailView(DetailView):
    model = Product
    template_name = 'merchstore/item.html'
