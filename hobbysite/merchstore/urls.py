from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ItemDetailView, item_list, item_create, ItemUpdateView

urlpatterns = [
    path("items", item_list, name="items"),
    path("item/<int:pk>", ItemDetailView.as_view(), name="item"),
    path("item/add", item_create, name="item-create"),
    path("item/<int:pk>/edit",
         login_required(ItemUpdateView.as_view()), name="item-update"),
]

app_name = "merchstore"
