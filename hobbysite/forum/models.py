from django.db import models
from django.urls import reverse
from user_management.models import Profile

class ThreadCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('forum:threads', args=[str(self.name)])

    class Meta:
        ordering = ['name']


class Thread(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile,
        null=True,
        on_delete=models.SET_NULL,
        related_name='threads'
    )
    category = models.ForeignKey(
        ThreadCategory,
        null=True,
        on_delete=models.SET_NULL,
        related_name='threads'
    )
    entry = models.TextField()
    image = models.ImageField(
        upload_to='thread_images/',
        blank=True,
        null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.thread_category.name}] {self.title}: Created on:{self.created_on} Last updated on:{self.updated_on} - {self.entry}"

    def get_absolute_url(self):
        return reverse('forum:thread', args=[str(self.pk)])

    class Meta:
        ordering = ['-created_on']


class Comment(models.Model):
    author = models.ForeignKey(
        Profile,
        null=True,
        on_delete=models.SET_NULL,
        related_name='forum_comments'
    )
    thread = models.ForeignKey(
        Thread,
        null=True,
        on_delete=models.CASCADE,
        related_name='forum_comments'
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['-created_on']