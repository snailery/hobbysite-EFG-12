from django.db import models
from django.urls import reverse

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('merchstore:items', args=[str(self.name)])
    
    class Meta:
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    prod_type = models.ForeignKey(
        ProductType,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"[{self.prod_type.name}] {self.name}: {self.desc} - {self.price} Bells"

    def get_absolute_url(self):
        return reverse('merchstore:item', args=[str(self.pk)])
    class Meta:
        ordering = ['name']
    
