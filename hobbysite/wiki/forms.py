from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'entry', 'category_type', 'header_image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-solid',
                'placeholder': 'Enter article title'
            }),
            'entry': forms.Textarea(attrs={
                'class': 'form-control form-control-solid',
                'placeholder': 'Write your article here...',
                'data-kt-autosize': 'true',
                'rows': '5'
            }),
            'category_type': forms.Select(attrs={
                'class': 'form-select form-select-solid',
                'data-control': 'select2',
                'data-placeholder': 'Select a category',
                'data-hide-search': 'true'
            }),
            'header_image': forms.ClearableFileInput(attrs={
                'class': 'form-control form-control-solid'
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']
        widgets = {
            'entry': forms.Textarea(attrs={
                'class': 'form-control form-control-solid',
                'placeholder': 'Write your comment...',
                'rows': 3
            }),
        }
