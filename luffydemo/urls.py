"""luffydemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, re_path, include
from django.contrib import admin
from app1 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'timer/', views.timer),
    url(r'^login/$', views.login, name="Login"),

    # 路由配置：  路径 --> 视图函数

    # re_path(r'^articles/2003/$', views.special_case_2003),
    # re_path(r'^articles/([0-9]{4})/$', views.year_archive),
    # # re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    # re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    # # re_path(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail)


    # 分发：
    re_path(r"app1/", include(("app1.urls", "app1"))),
    re_path(r"app2/", include(("app2.urls", "app2"))),
    re_path(r"ajaxdemo/", include(("ajaxdemo.urls", "ajaxdemo"))),



]
