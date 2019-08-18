from django.shortcuts import render, HttpResponse
from ajaxdemo.models import *
# Create your views here.


def index(request):

    return render(request, "./ajaxdemo/index.html")


def test_ajax(request):
    print(request.GET)
    return HttpResponse("hello world")


def cal(request):
    print(request.POST)
    n1 = request.POST.get("n1")
    n2 = request.POST.get("n2")
    ret = int(n1) + int(n2)
    return HttpResponse(ret)


def login(request):
    print("ajaxdemo.login")

    print(request.POST)
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    user_obj = User.objects.filter(name=user, pwd=pwd).first()

    res = {"user": None, "msg": None}
    if user_obj:
        res['user'] = user.name
    else:
        res['msg'] = "username or password wrong!"

    import json
    return HttpResponse(json.dumps(res))


def file_put(request):
    if request.method == "POST":
        print("head", request.headers)
        print("body", request.body)  # 请求报文中的请求体  json
        print("post", request.POST)  # if contentType == urlencoded: request.POST 才有数据
        print(request.FILES)  # 获取上传文件电对象
        # 上传文件，保存在本地
        # file_obj = request.FILES.get("avatar")
        # with open(file_obj.name, "wb") as f:
        #     for line in file_obj:
        #         f.write(line)
        return HttpResponse("OK")

    return render(request, "ajaxdemo/file_put.html")

'''
请求首行
请求头
...
ContentType:urlencode
请求体()
'''
