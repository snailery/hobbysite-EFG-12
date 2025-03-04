from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Article

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'article.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles.html'
