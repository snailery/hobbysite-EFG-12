from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect, reverse
from .models import Product, ProductType
from user_management.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import ProductForm


# class ItemListView(ListView):
#     model = Product
#     template_name = 'merchstore/items.html'


class ItemDetailView(DetailView):
    model = Product
    template_name = 'merchstore/item.html'


def item_list(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(id=request.user.id)
        your_products = Product.objects.filter(owner=profile)
        all_products = Product.objects.exclude(owner=profile)
    else:
        all_products = Product.objects.all()
        your_products = []

    ctx = {
        "all_products": all_products,
        "your_products": your_products
    }
    return render(request, 'merchstore/items.html', ctx)


@login_required(login_url='/accounts/login/')
def item_create(request):
    prod_types = ProductType.objects.all()
    status_choices = Product.status.field.choices

    if request.method == "POST":
        form = ProductForm(request.POST, initial={"status": "available"})

        if form.is_valid():
            p = Product()
            p.name = request.POST.get("name")
            p.owner = request.user.profile
            p.desc = request.POST.get("desc")
            p.price = request.POST.get("price")
            p.stock = request.POST.get("stock")
            p.prod_type = ProductType.objects.get(pk=request.POST.get("prod_type"))
            p.save()

            return redirect(reverse("merchstore:items"))
        else:
            print(form.errors.as_data())

    else:
        form = ProductForm(initial={"status": "available" })


    ctx = {
        "prod_types": prod_types,
        "status_choices": status_choices,
        "form": form
    }
    
    return render(request, 'merchstore/item-create.html', ctx)