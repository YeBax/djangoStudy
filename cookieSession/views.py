from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

from .models import UserInfo


def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        user = UserInfo.objects.filter(user=user, pwd=pwd).first()

        if user:
            # 登陆成功

            '''
            响应体:
            return HttpResponse()
            return render()
            return redirect()
            '''
            response = HttpResponse("登录成功!")
            # response.set_cookie("is_login",True,max_age=15)
            response.set_cookie("is_login", True)
            import datetime
            # date=datetime.datetime(year=2019,month=8,day=21,hour=23,minute=5, second=10)
            # response.set_cookie("username",user.user,expires=date)
            response.set_cookie("username", user.user, path="/cookiesession/index/")
            return response

    return render(request, "cookiesession/login.html")


def index(request):
    print("index:", request.COOKIES)

    is_login = request.COOKIES.get("is_login")

    if is_login:
        username = request.COOKIES.get("username")

        import datetime

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        last_time = request.COOKIES.get("last_visit_time", "")
        response = render(request, "cookiesession/index.html", {"username": username, "last_visit_time": last_time})
        response.set_cookie("last_visit_time", now)
        return response

    else:
        return redirect("/cookiesession/login/")


def test(request):
    print("test:", request.COOKIES)

    return HttpResponse("test!")
