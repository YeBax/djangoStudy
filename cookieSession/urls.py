from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path("login/", views.login),
    path("index/", views.index),
    path("test/", views.test),
    path("login_session/", views.login_session),
    path("index_session/", views.index_session),
    path("logout/", views.logout)

]