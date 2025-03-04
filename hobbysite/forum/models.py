from django.db import models
from django.urls import reverse

# Create your models here.
class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('forum:threads', args=[str(self.name)])
    
    class Meta:
        ordering = ['name']


class Post(models.Model):
    title = models.CharField(max_length=255)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    post_category = models.ForeignKey(
        PostCategory,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"[{self.post_type.name}] {self.title}: Created on:{self.created_on} Last updated on:{self.updated_on} - {self.entry}"

    def get_absolute_url(self):
        return reverse('forum:thread', args=[str(self.pk)])
    class Meta:
        ordering = ['-created_on']
