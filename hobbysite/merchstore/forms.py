from django import forms
from .models import Product, ProductType, Transaction

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "desc", "stock", "price", "prod_type", "status")
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control form-control-solid",
                    "placeholder": "Wooden Chair"
                }
            ),
            "desc": forms.Textarea(
                attrs={
                    "class": "form-control form-control-solid",
                    "data-kt-autosize": "true",
                    "placeholder": "Describe your product",
                    "rows": "3"
                }
            ),
            "stock": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "00",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "00.00",
                }
            ),
            "prod_type": forms.Select(
                attrs={
                    "class": "form-select form-select-solid",
                    "data-control": "select2",
                    "data-placeholder": "Select an option",
                    "data-hide-search": "true"
                }
            ),
            "status": forms.Select(
                attrs={
                    "class": "form-select form-select-solid",
                    "data-control": "select2",
                    "data-placeholder": "Select an option",
                    "data-hide-search": "true"
                }
            )
        }
