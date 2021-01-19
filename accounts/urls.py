from django.urls import path
from . import views

urlpatterns = [
    path("create-role/", views.createRole, name="createRole"),
    path("assign-role/", views.assignRole, name="assignRole"),
    path("assign-permission/", views.assignPermission, name="assignPermission"),
]
