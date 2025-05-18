from django.contrib import admin
from .models import ArticleCategory, Article, Comment

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)
    ordering = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_on', 'updated_on',)
    search_fields = ('title', 'entry',)
    list_filter = ('category', 'created_on',)
    ordering = ('-created_on',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'article', 'created_on', 'updated_on')
    search_fields = ('entry', 'author__user__username', 'article__title')
    list_filter = ('created_on', 'article')
    ordering = ('created_on',)

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
