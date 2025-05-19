from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from .models import Article, ArticleCategory, Comment
from .forms import ArticleForm, ArticleCategoryForm, ArticleUpdateForm, ArticleCommentForm

def view_article_list(request):
    user_profile = getattr(request.user, 'profile', None)
    own_articles = Article.objects.filter(author=user_profile) if user_profile else Article.objects.none()

    categories = ArticleCategory.objects.all().prefetch_related(
        Prefetch(
            'articles',
            queryset=Article.objects.exclude(author=user_profile) if user_profile else Article.objects.all()
        )
    )

    context = {
        'articles_by_user': own_articles,
        'categories': categories,
    }
    return render(request, 'blog/article_list.html', context)

def view_article_detail(request, num):
    article = get_object_or_404(Article, pk=num)
    user_profile = getattr(request.user, 'profile', None)
    is_author = user_profile == article.author

    related_articles = Article.objects.filter(author=article.author).exclude(pk=article.pk)

    comments = Comment.objects.filter(article=article).order_by('created_on')

    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = ArticleCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = user_profile
            new_comment.article = article
            new_comment.save()
            return redirect('blog:article_detail', num=article.pk)
    else:
        comment_form = ArticleCommentForm()

    context = {
        'article': article,
        'is_author': is_author,
        'related_articles': related_articles,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'blog/article_detail.html', context)

@login_required
def create_article(request):
    if request.method == 'POST':
        if 'submit_article' in request.POST:
            article_form = ArticleForm(request.POST, request.FILES)
            category_form = ArticleCategoryForm()
            if article_form.is_valid():
                new_article = article_form.save(commit=False)
                new_article.author = request.user.profile
                new_article.save()
                return redirect('blog:article_list')
        elif 'submit_category' in request.POST:
            category_form = ArticleCategoryForm(request.POST)
            article_form = ArticleForm()
            if category_form.is_valid():
                category_form.save()
                return redirect('blog:article_list')
    else:
        article_form = ArticleForm()
        category_form = ArticleCategoryForm()

    context = {
        'article_form': article_form,
        'category_form': category_form,
    }
    return render(request, 'blog/article_create.html', context)

@login_required
def update_article(request, num):
    article = get_object_or_404(Article, pk=num)
    if request.user.profile != article.author:
        return redirect('blog:article_detail', num=num)

    if request.method == 'POST':
        update_form = ArticleUpdateForm(request.POST, request.FILES, instance=article)
        if update_form.is_valid():
            update_form.save()
            return redirect('blog:article_detail', num=article.pk)
    else:
        update_form = ArticleUpdateForm(instance=article)

    context = {
        'update_form': update_form,
        'article': article,
    }
    return render(request, 'blog/article_edit.html', context)
