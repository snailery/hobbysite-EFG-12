from django.contrib import admin
from .models import Product, ProductType


class ProductInline(admin.TabularInline):
    model = Product


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    inlines = [ProductInline]


class ProductAdmin(admin.ModelAdmin):
    model = Product
    search_fields = ("name", )
    list_display = ("name", "desc", "price", "prod_type")

    fieldsets = [
        ("Details", {
            "fields": [
                ("name", "desc", "price"), "prod_type"
            ]
        }),
    ]


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
