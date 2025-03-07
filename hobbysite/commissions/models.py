from django.db import models
from django.urls import reverse


class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    people_required = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('commissions:commission', args=[str(self.pk)])

    class Meta:
        ordering = ['created_on']


class Comment(models.Model):
    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"[{self.commission}] {self.entry}"

    def get_absolute_url(self):
        return reverse('commissions:commission', args=[str(self.commission.pk)])

    class Meta:
        ordering = ['-created_on']
