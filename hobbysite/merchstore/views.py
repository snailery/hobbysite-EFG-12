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
        ctx['form'] = TransactionForm(
            initial={"amount": self.request.session.get("amount")})
        return ctx

    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)

        if form.is_valid():
            if not request.user.is_authenticated:
                request.session["amount"] = request.POST.get("amount")
            
            return test_post(request, self.get_object().pk)
        else:
            print(form.errors.as_data())
        

@login_required
def test_post(request, p_pk):
    if request.session.get("amount"):
        del request.session["amount"]
    
    t = Transaction()
    p = Product.objects.get(pk=p_pk)
    t.buyer = request.user.profile
    t.amount = int(request.POST.get("amount"))
    p.stock -= t.amount
    
    if p.stock < 1:
        # p.status = Product.PRODUCT_STATUS["OUT"]
        p.status = "OUT"

    p.save()
    t.product = p
    t.save()

    return redirect(reverse("merchstore:cart"))
    


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
        p = form.save(commit=False)

        if p.stock == 0:
            p.status = "OUT"
        elif p.stock > 0 and p.status == "OUT":
            p.status = "AVL"

        super(ItemUpdateView, self).form_valid(form)
        return redirect(self.get_success_url())
    
    def get_success_url(self):
       pk = self.kwargs["pk"]
       return reverse("merchstore:item", kwargs={"pk": pk})