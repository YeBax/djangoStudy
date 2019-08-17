# -*- coding: utf-8 -*-
"""
-----------------------------------
@Project : luffydemo
@File    : my_tag_fliter.py
@Author  : Yebax
@Time    : 2019/8/12 23:59
-----------------------------------
    ==Oh Captain! My Captain!==
"""
from django import template

register = template.Library()


@register.filter
def multi_filter(x, y):
    return x * y


@register.simple_tag
def multi_tag(x, y):
    return x * y


