from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post


class ItemListView(ListView):
    model = Post
    template_name = 'threads.html'


class ItemDetailView(DetailView):
    model = Post
    template_name = 'thread.html'
