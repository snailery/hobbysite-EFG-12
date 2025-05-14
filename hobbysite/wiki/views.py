from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Article, ArticleCategory, Comment
from .forms import ArticleForm, CommentForm
from user_management.models import Profile

def index(request):
    return HttpResponse("Wiki Home")

class ArticleListView(ListView):
    model = Article
    template_name = 'wiki/articles.html'
    queryset = Article.objects.order_by('category_type')

def render_articles(request):
    categories = ArticleCategory.objects.all()
    if request.user.is_authenticated:
        ctx = {
            'my_articles': Article.objects.filter(author=Profile.objects.get(user=request.user)),
            'all_articles': categories
        }
    else:
        ctx = {
            'all articles': categories
        }

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'wiki/article.html'

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        ctx = super().get_context_data(**kwargs)
        article = self.object

        ctx['article'] = article
        ctx['comment_form'] = CommentForm()

        similar_articles = Article.objects.filter(category=article.category_type).exclude(pk=article.pk)
        ctx['similar_articles'] = similar_articles

        return ctx
    
    def post(self, request, *args, **kwargs):
        author = Profile.objects.get(user=request.user)
        article = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.author = author
            comment.article = article
            comment.entry = form.cleaned_data.get('entry')
            comment.save()
            return self.get(request, *args, **kwargs)
        ctx = self.get_context_data(**kwargs)
        return self.render_to_response(ctx)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'wiki/article.html'
    exclude = ['created_on', 'updated_on', 'author']

    def get_success_url(self):
        return reverse_lazy('wiki:article_detail', kwargs={ 'pk': self.object.pk})
    
    def form_valid(self, form):
        author = Profile.objects.get(user=self.request.user)
        form.instance.author = author
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        author = Profile.objects.get(user=self.request.user)
        ctx = super().get_context_data(**kwargs)
        ctx['create_article'] = ArticleForm(initial={'author': author})
        return ctx

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'wiki/article.html'

    def get_success_url(self):
        return reverse_lazy('wiki:article_detail', kwargs={ 'pk': self.object.pk})
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['article'] = Article.objects.get(pk=self.object.pk)
        return ctx

