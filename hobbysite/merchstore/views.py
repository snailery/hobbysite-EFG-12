from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Product
from user_management.models import Profile


# class ItemListView(ListView):
#     model = Product
#     template_name = 'merchstore/items.html'


class ItemDetailView(DetailView):
    model = Product
    template_name = 'merchstore/item.html'


def item_list(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(id=request.user.id)
        your_products = Product.objects.exclude(owner=profile)
        all_products = Product.objects.filter(owner=profile)
    else:
        all_products = Product.objects.all()
        your_products = []

    ctx = {
        "all_products": all_products,
        "your_products": your_products
    }
    return render(request, 'merchstore/items.html', ctx)
