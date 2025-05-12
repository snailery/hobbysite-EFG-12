from django.urls import path
from .views import passport

urlpatterns = [
    path("<str:username>/", passport, name="username"),
]

app_name = "user_management"
