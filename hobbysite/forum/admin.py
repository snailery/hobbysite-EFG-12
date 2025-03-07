from django.contrib import admin
from .models import Post, PostCategory


class PostInline(admin.TabularInline):
    model = Post


class PostCategoryAdmin(admin.ModelAdmin):
    model = PostCategory
    inlines = [PostInline]


admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post)
