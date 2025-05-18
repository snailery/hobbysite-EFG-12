from django.db import models
from django.urls import reverse
from profile.models import Profile


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wiki:articles', args=[str(self.name)])

    class Meta:
        ordering = ['name']


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, related_name='wiki_author', blank=True)
    entry = models.TextField()
    header_image = models.ImageField(upload_to='images/wiki', null=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    category_type = models.ForeignKey(ArticleCategory, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('wiki:article_detail', args=[str(self.pk)])

    class Meta:
        ordering = ['-created_on']

class Comment(models.Model):
    author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, related_name='wiki_comment_author')
    article = models.ForeignKey(Article, null=False, on_delete=models.CASCADE)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"[{self.author.username if self.author else 'Deleted User'}]  (Created On: {self.created_on} Last Updated On: {self.updated_on}) - {self.entry}"

    class Meta:
        ordering = ['created_on']
