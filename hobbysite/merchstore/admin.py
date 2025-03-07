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
        # fieldsets is a list of tuples where the syntax is:
        # ('label of the field', {'fields': [<list of fields>]})
        ("Details", {
            "fields": [
                # the tuple puts these fields in a single line
                ("name", "desc", "price"), "prod_type"
            ]
        }),
    ]


# Register your models here.
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
