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


def login_session(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        user = UserInfo.objects.filter(user=user, pwd=pwd).first()

        if user:
            request.session["is_login"] = True
            request.session["username"] = user.user

            import datetime

            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            request.session["last_visit_time"] = now





            '''
            1 生成一个随机字符串     123456abc
            2 response.set_cookie("sessionid", "123456abc")
            3 在django-session表中创建一条记录
                session-key   session-data
                123456abc       {"is_login":True, "username":"yuan"}
            '''

            return HttpResponse("登录成功！")

    return render(request, "cookiesession/login.html")


def index_session(request):
    print(request.session.get("is_login"))
    print(request.session.keys())
    print(request.session.items())
    print(request.session.get("username", "yebax"))
    '''
    1 request.COOKIE.get("session") 
    2 django-session表中创建一条记录：
            session-key   session-data
            123456abc       {"is_login":True, "username":"yuan"}-key
        obj = django-session.objects.filter(session-key=....)
    3 obj.session-data.get('is_login')
    
    '''
    is_login = request.session.get("is_login")
    if not is_login:
        return redirect("/cookiesession/login_session/")
    username = request.session.get("username")
    last_visit_time = request.session.get("last_visit_time")
    return render(request, "cookiesession/index.html", locals())


def logout(request):

    # del request.session["is_login"]

    request.session.flush()
    '''
    1 request.COOKIE.get("sessionid")
    2 django-session.objects.filter(session_key=....).delete()
    3 response.delete_cookie("cookie_key", path="/", domain=name)
    '''
    return redirect("/cookiesession/login_session/")


'''
Django默认支持Session，并且默认是将Session数据存储在数据库中，即：django_session 表中。

a. 配置 settings.py

    SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）

    SESSION_COOKIE_NAME ＝ "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
    SESSION_COOKIE_PATH ＝ "/"                               # Session的cookie保存的路径（默认）
    SESSION_COOKIE_DOMAIN = None                             # Session的cookie保存的域名（默认）
    SESSION_COOKIE_SECURE = False                            # 是否Https传输cookie（默认）
    SESSION_COOKIE_HTTPONLY = True                           # 是否Session的cookie只支持http传输（默认）
    SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周）（默认）
    SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期（默认）
    SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存（默认）
练习

'''