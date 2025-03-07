from django.urls import path
from .views import ItemListView, ItemDetailView

urlpatterns = [
    path("threads", ItemListView.as_view(), name="threads"),
    path("threads/<int:pk>", ItemDetailView.as_view(), name="thread")
]

app_name = "forum"
