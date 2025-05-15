from django.urls import path
from .views import ItemDetailView, item_list, item_create

urlpatterns = [
    path("items", item_list, name="items"),
    path("item/<int:pk>", ItemDetailView.as_view(), name="item"),
    path("item/add", item_create, name="item-create")
]

app_name = "merchstore"
