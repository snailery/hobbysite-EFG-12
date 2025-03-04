from django.db import models
from django.urls import reverse

# Create your models here.
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
    entry = models.TextField()
    created_on = models.DateTimeField(False, True, editable=False)
    updated_on = models.DateTimeField(True, True, editable=False)
    categoryType = models.ForeignKey(
        ArticleCategory,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"[{self.category_type.name}] {self.title} (Created On: {self.created_on} Last Updated On: {self.updated_on}) - {self.entry}"
    

    def get_absolute_url(self):
        return reverse('wiki:article', args=[str(self.pk)])
    class Meta:
        ordering = ['-created_on']
    
