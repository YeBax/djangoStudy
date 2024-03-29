from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path("login/", views.login),
    path("index/", views.index),
    path("logout/", views.logout),
    path("reg/", views.reg),
    path("order/", views.order),
]