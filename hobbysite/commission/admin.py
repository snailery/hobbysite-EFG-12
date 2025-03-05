from django.contrib import admin
from .models import Commission, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class CommissionAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment)
