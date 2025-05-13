from django.db import models
from django.urls import reverse
from user_management.models import Profile


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
    PRODUCT_STATUS = {
        "AVL": "Available",
        "SAL": "On Sale",
        "OUT": "Out of Stock",
    }

    name = models.CharField(max_length=255)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    status = models.CharField(max_length=3, choices=PRODUCT_STATUS, default="AVL")
    prod_type = models.ForeignKey(ProductType, null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(Profile, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.prod_type.name}] {self.name}: {self.desc} - {self.price} Bells"

    def get_absolute_url(self):
        return reverse('merchstore:item', args=[str(self.pk)])

    class Meta:
        ordering = ['name']


class Transaction(models.Model):
    TRANSACTION_STATUS = {
        "CRT": "On Cart",
        "PAY": "To Pay",
        "SHP": "To Ship",
        "RCV": "To Receive"
    }

    buyer = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField()
    status = models.CharField(max_length=3, null=True, choices=TRANSACTION_STATUS)

    def __str__(self):
        return f"[{self.status}] {self.product.name}: x{self.amt} purchased by {self.buyer.display_name}"
