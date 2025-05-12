from django.urls import path
from .views import ItemDetailView, item_list

urlpatterns = [
    path("items", item_list, name="items"),
    path("item/<int:pk>", ItemDetailView.as_view(), name="item")
]

app_name = "merchstore"
