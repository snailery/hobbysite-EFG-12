from django.urls import path
from .views import ItemListView, ItemDetailView

urlpatterns = [
    path("items", ItemListView.as_view(), name="items"),
    path("item/<int:pk>", ItemDetailView.as_view(), name="item")
]

app_name = "merchstore"
