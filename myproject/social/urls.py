# social/urls.py

from django.urls import path
from .views import dashboard, profile_list

app_name = "social"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
]