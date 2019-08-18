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
from pageDemo import views

urlpatterns = [
    path("index/", views.index),


]