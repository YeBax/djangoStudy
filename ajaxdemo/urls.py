# -*- coding: utf-8 -*-
"""
-----------------------------------
@Project : luffydemo
@File    : urls.py
@Author  : Yebax
@Time    : 2019/8/11 23:00
-----------------------------------
    ==Oh Captain! My Captain!==
"""
__author__ = "Yebax"

from django.urls import path, re_path
from ajaxdemo import views

urlpatterns = [
    path("index/", views.index),
    path("test_ajax/", views.test_ajax, name="text_ajax"),
    path("cal/", views.cal),
    path("login/", views.login),
    path("file_put/", views.file_put)

]