from django.urls import path, re_path, include

from . import views

urlpatterns = [
    re_path("reg/", views.reg),

]