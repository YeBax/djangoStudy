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
from app2 import views

urlpatterns = [
    re_path("index/", views.index, name="index"),
    path("orders/", views.orders),
    path("query/", views.query)
    
]