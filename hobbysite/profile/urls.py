from django.urls import path
from .views import passport

urlpatterns = [
    path("<str:username>/", passport, name="profile"),
]

app_name = "profile"
