# social/urls.py

from django.urls import path
from .views import dashboard

app_name = "social"

urlpatterns = [
    path("", dashboard, name="dashboard"),
]