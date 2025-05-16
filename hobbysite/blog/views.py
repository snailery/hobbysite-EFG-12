from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Prefetch
from django.contrib.auth.decorators import login_required
from .models import Article, ArticleCategory, Comment
from .forms import ArticleForm, ArticleCategoryForm, ArticleUpdateForm, ArticleCommentForm

@login_required
def view_article_list(request):
    profile = request.user.profile
    own_articles = Article.objects.filter(author=profile)
    other_articles = Article.objects.exclude(author=profile)

    grouped_categories = ArticleCategory.objects.prefetch_related(
        Prefetch('articles', queryset=other_articles)
    )

    context = {
        'own_articles': own_articles,
        'articles': other_articles,
        'categories': grouped_categories,
    }

    return render(request, 'article_list.html', context)


def view_article_detail(request, num):
    article = get_object_or_404(Article, pk=num)
    all_comments = Comment.objects.filter(article=article).order_by('-created_on')
    similar_posts = Article.objects.filter(author=article.author).exclude(pk=article.pk)

    if request.method == "POST":
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.article = article
            if request.user.is_authenticated:
                new_comment.author = request.user.profile
            new_comment.save()
            return redirect('article_detail', num=article.pk)
    else:
        form = ArticleCommentForm()

    context = {
        'article': article,
        'comments': all_comments,
        'related_articles': similar_posts,
        'comment_form': form,
    }

    return render(request, 'article_detail.html', context)

@login_required
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        cat_form = ArticleCategoryForm(request.POST)

        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.author = request.user.profile
            new_article.save()
            return redirect('article_list')

        if cat_form.is_valid():
            cat_form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
        cat_form = ArticleCategoryForm()

    return render(request, 'article_create.html', {
        'article_form': form,
        'category_form': cat_form,
    })


@login_required
def update_article(request, num):
    article = get_object_or_404(Article, pk=num)

    if article.author != request.user.profile:
        return redirect('article_list')

    if request.method == "POST":
        form = ArticleUpdateForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', num=article.pk)
    else:
        form = ArticleUpdateForm(instance=article)

    return render(request, 'article_update.html', {
        'article': article,
        'update_form': form,
    })
