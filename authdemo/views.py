from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        user = auth.authenticate(username= user, password=pwd)  # 如果验证成功 返回 user对象 否则返回none

        if user:
            auth.login(request, user)  # request.user:当前登录对象
            next_url = request.GET.get("next", "authdemo/index/")
            print(next_url)
            return redirect(next_url)

    return render(request, "authdemo/login.html")


@login_required
def index(request):

    # print("request:", request.user.username)
    # print("request:", request.user.id)
    # print("request:", request.user.is_anonymous)
    #
    # if request.user.is_anonymous:
    #     return redirect("/authdemo/login/")
    #
    # username = request.user.username

    return render(request, "authdemo/index.html", locals())


def logout(request):

    auth.logout(request)

    return redirect("/authdemo/login/")


def reg(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        # User.objects.create(username=user, password=pwd)  #  密码明文，不加密
        User.objects.create_user(username=user, password=pwd)   # 用auth方法 密码加密

        return redirect("/authdemo/index/")

    return render(request, "authdemo/reg.html")


@login_required
def order(request):

    return render(request, "authdemo/order.html")
