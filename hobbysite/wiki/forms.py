from django import forms
from .models import ArticleCategory, Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'entry', 'category_type'] 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["entry"]

