from django.urls import path
from .views import ItemListView, ItemDetailView

urlpatterns = [
    path("articles", ItemListView.as_view(), name="articles"),
    path("article/<int:pk>", ItemDetailView.as_view(), name="article")
]

app_name = "merchstore"
