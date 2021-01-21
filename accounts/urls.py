from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
urlpatterns = [
    path("create-role/", views.createRole, name="createRole"),
    path("assign-role/", views.assignRole, name="assignRole"),
    path("assign-permission/", views.assignPermission, name="assignPermission"),
    path('',include(router.urls)),
    path('login/', views.UserLoginApiView.as_view())
]
