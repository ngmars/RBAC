from django.urls import path
from . import views

urlpatterns = [
    path("create-role/", views.createRole, name="createRole"),
]
