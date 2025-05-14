from django import forms
from .models import ArticleCategory, Article, Comment


class ArticleForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=ArticleCategory.objects.all(), empty_label="Choose a category")
    class Meta:
        model = Article
        fields = ['title', 'entry', 'category'] 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["entry"]

