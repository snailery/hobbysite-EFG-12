from django.contrib import admin
from .models import Article, ArticleCategory


class ArticleInline(admin.TabularInline):
    model = Article


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [ArticleInline]


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    search_fields = ("title", )
    list_display = ("title", "category_type", "created_on", "updated_on", "entry")

    fieldsets = [
        # fieldsets is a list of tuples where the syntax is:
        # ('label of the field', {'fields': [<list of fields>]})
        ("Details", {
            "fields": [
                # the tuple puts these fields in a single line
                ("category_type", "name", "created_on", "updated_on"), "entry"
            ]
        }),
    ]


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
