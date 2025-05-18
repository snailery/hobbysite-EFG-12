from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
from .views import ItemDetailView, item_list, item_create, ItemUpdateView, cart, transactions

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="merchstore:items",
         permanent=False), name="index"),
    path("items", item_list, name="items"),
    path("item/<int:pk>", ItemDetailView.as_view(), name="item"),
    path("item/add", item_create, name="item-create"),
    path("item/<int:pk>/edit",
         login_required(ItemUpdateView.as_view()), name="item-update"),
    path("cart", cart, name="cart"),
    path("transactions", transactions, name="transactions")
]

app_name = "merchstore"
