from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render

from .models import Article
from .forms import ArticleForm


class ArticleListView(ListView):
    model = Article
    template_name = 'wiki/articles.html'
    queryset = Article.objects.order_by('category_type')


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'wiki/article.html'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'wiki/article.html'
    success_url = 'wiki/articles.html'
    exclude = ['created_on', 'updated_on', 'author'] #TODO: category field dropdown

def article_create(request):
    new_article = ArticleForm
    return render(request, 'wiki/article/add', {'form': new_article})
    

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'wiki/article.html'
    success_url = 'wiki/article.html'

