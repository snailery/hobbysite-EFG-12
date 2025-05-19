from django.contrib import admin
from .models import Product, ProductType, Transaction


class ProductInline(admin.TabularInline):
    model = Product


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    inlines = [ProductInline]


class ProductAdmin(admin.ModelAdmin):
    model = Product
    search_fields = ("name", )
    list_display = ("name", "desc", "price", "stock",
                    "status", "prod_type", "owner")

    fieldsets = [
        ("Details", {
            "fields": [
                ("name", "desc", "price", "stock", "status", "image"), "prod_type", "owner"
            ]
        }),
    ]


class TransactionInline(admin.TabularInline):
    model = Transaction


class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    search_fields = ("product", )
    list_display = ("product", "amount", "buyer", "status", "created_on")

    fieldsets = [
        ("Details", {
            "fields": [
                "product", ("amount", "status"), "buyer"
            ]
        }),
    ]


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)
