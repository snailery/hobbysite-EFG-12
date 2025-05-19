from django import forms
from .models import Product, ProductType, Transaction

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["image"].required = False

    class Meta:
        model = Product
        fields = ("name", "desc", "stock", "price", "prod_type", "status", "image")
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
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "d-none"
                }
            )
        }


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ("amount", )
        widgets = {
            "amount": forms.TextInput(
                attrs={
                    "class": "form-control form-control-solid border-0 ps-12 fw-bold",
                    "data-kt-dialer-control": "input",
                    "placeholder": "0",
                }
            ),
        }