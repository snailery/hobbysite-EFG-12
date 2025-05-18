from django.urls import path
from .views import (
    view_article_list,
    view_article_detail,
    create_article,
    update_article,
)

app_name = 'blog'

urlpatterns = [
    path('articles/', view_article_list, name='article_list'),
    path('article/<int:num>/', view_article_detail, name='article_detail'),
    path('article/add/', create_article, name='article_create'),
    path('article/<int:num>/edit/', update_article, name='article_update'),
]
