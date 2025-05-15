from django import forms
from .models import Article, ArticleCategory, ArticleComment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']

class ArticleCategoryForm(forms.ModelForm):
    class Meta:
        model = ArticleCategory
        fields = '__all__'

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']

class ArticleCommentForm(forms.ModelForm):
    entry = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'rows': 4,
                'placeholder': 'Write your comment here...'
            }
        )
    )

    class Meta:
        model = ArticleComment
        fields = ['entry']
