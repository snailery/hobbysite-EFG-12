from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, FormMixin
from django.shortcuts import render, redirect, reverse
from profile.models import Profile
from django.contrib.auth.decorators import login_required

from .forms import ProductForm, TransactionForm
from .models import Product, ProductType, Transaction


@login_required
def transactions(request):
    profile = Profile.objects.get(id=request.user.id)
    transactions = Transaction.objects.exclude(buyer=profile)

    ctx = {
        "header": "Products Sold",
        "transactions": transactions,
    }

    return render(request, "merchstore/transactions.html", ctx)


@login_required
def cart(request):
    profile = Profile.objects.get(id=request.user.id)
    transactions = Transaction.objects.filter(buyer=profile)

    ctx = {
        "header": "Your Cart",
        "transactions": transactions,
    }

    return render(request, "merchstore/transactions.html", ctx)


class ItemDetailView(FormMixin, DetailView):
    model = Product
    template_name = 'merchstore/item.html'
    form_class = TransactionForm

    def get_success_url(self):
        return reverse("merchstore:items")
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = TransactionForm()
        return ctx

    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)

        if form.is_valid():
            t = Transaction()
            p = Product.objects.get(pk=self.get_object().pk)
            t.buyer = request.user.profile
            t.amount = int(request.POST.get("amount"))
            p.stock -= t.amount
            p.save()

            t.product = p
            t.save()

            return redirect(reverse("merchstore:items"))
        else:
            print(form.errors.as_data())
            self.object_list = self.get_queryset(**kwargs)
            ctx = self.get_context_data(**kwargs)
            ctx['form'] = form

            return self.render_to_response(ctx)


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


@login_required
def item_create(request):
    prod_types = ProductType.objects.all()
    status_choices = Product.status.field.choices

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, initial={"status": "available"})

        if form.is_valid():
            p = Product()
            p.name = request.POST.get("name")
            p.owner = request.user.profile
            p.desc = request.POST.get("desc")
            p.price = request.POST.get("price")
            p.stock = request.POST.get("stock")
            p.prod_type = ProductType.objects.get(
                pk=request.POST.get("prod_type"))
            if request.FILES:
                p.image = request.FILES["image"]
            p.save()

            return redirect(reverse("merchstore:items"))
        else:
            print(form.errors.as_data())

    else:
        form = ProductForm(initial={"status": "available"})

    ctx = {
        "prod_types": prod_types,
        "status_choices": status_choices,
        "form": form
    }

    return render(request, 'merchstore/item-form.html', ctx)


class ItemUpdateView(UpdateView):
    model = Product
    template_name = 'merchstore/item-form.html'
    form_class = ProductForm

    def form_valid(self, form):
        instance = form.save(commit=False)

        if instance.stock == 0:
            instance.status = "OUT"
        elif instance.stock > 0 and instance.status == "OUT":
            instance.status = "AVL"

        super(ItemUpdateView, self).form_valid(form)
        return redirect(self.get_success_url())
    
    def get_success_url(self):
       pk = self.kwargs["pk"]
       return reverse("merchstore:item", kwargs={"pk": pk})