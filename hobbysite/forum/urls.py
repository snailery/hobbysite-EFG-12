from django.urls import path
from .views import ItemListView, ItemDetailView

urlpatterns = [
    path("threads", ItemListView.as_view(), name="items"),
    path("threads/<int:pk>", ItemDetailView.as_view(), name="item")
]

app_name = "forum"