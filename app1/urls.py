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
from app1 import views

urlpatterns = [
    re_path(r'^articles/2003/$', views.special_case_2003, name="s_c_2003"),
    re_path(r'^articles/([0-9]{4})/$', views.year_archive, name="y_a"),
    # re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    # re_path(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail)
    re_path("index/$", views.index, name="index"),
    path("index2/", views.index2, name="index2"),
]