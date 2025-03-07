from django.contrib import admin
from .models import Post, PostCategory


class PostInline(admin.TabularInline):
    model = Post


class PostCategoryAdmin(admin.ModelAdmin):
    model = PostCategory
    inlines = [PostInline]


class PostAdmin(admin.ModelAdmin):
    model = Post
    search_fields = ("title", )
    list_display = ("title", "entry", "created_on", "updated_on")

    fieldsets = [
        ("Details", {
            "fields": [
                ("title", "entry", "created_on", "updated_on"), "post_type"
            ]
        }),
    ]


admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)
