from django.shortcuts import render, HttpResponse

# Create your views here.
from django.urls import reverse


def timer(request):

    import time
    ctime=time.time()

    # url=reverse("s_c_2003")
    # url=reverse("y_a",args=(3333,)) # app01/articles/([0-9]{4})/


    # print(url)


    return render(request,"timer.html",{"date":ctime})



from django.urls import reverse


def special_case_2003(request):
    url = reverse("s_c_2003")
    print(url)

    return HttpResponse("special_case_2003")


def year_archive(request, year):
    url = reverse("y_a", args=(year,))
    print(url)
    return HttpResponse("year:%s" % year)


def month_archive(request, month, year):
    return HttpResponse("year: %s, month: %s" % (year, month))


def login(request):
    print(request.method)

    if request.method == "GET":
        print(request.GET)
        return render(request, "login.html")

    if request.method == "POST":
        print(request.POST)

        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        if user == "a" and pwd == "123":
            return HttpResponse("登录成功！")
        else:
            return HttpResponse("登录失败")


def index(request):
    url = reverse("app1:index")
    print(url)
    print(request.GET)
    print(request.POST)
    print(request.path)
    print(request.get_full_path())

    import time
    ctime = time.time()
    # return HttpResponse("<h1>index1 OK</h1>")
    return render(request, "index.html", {"timer": ctime})  # index.html 模板文件


def index2(request):
    """
    模板语法 ：
        变量：{{ }}
            1 深度查询  句点符
            2 过滤器 {{val| filter_name:参数}}
        标签：{% %}
    :param request:
    :return:
    """
    name = "yebax"
    i = 10
    l = [111,222,333]

    info = {"name":"tang", "age":22}

    b = True

    class Person(object):

        def __init__(self, name, age):
            self.name = name
            self.age =age

    alex = Person("alex", 33)
    yebax = Person("yebax", 22)
    person_list = [alex, yebax]
    person_list1 = []


    ##################### 过滤器
    import datetime
    now = datetime.datetime.now()
    file_size = 12335431
    str_name = 'aaaaYangManbbbb'
    text = "央视网消息（焦点访谈）：人民健康是民族昌盛和国家富强的重要标志，习近平总书记的“没有全民健康，就没有全面小康”的重要论述，赢得了全社会的强烈共鸣。党的十九大进一步做出了实施健康中国战略的重大决策部署，强调坚持预防为主，倡导健康文明生活方式，预防控制重大疾病。不久前国务院印发了《关于实施健康中国行动的意见》，从国家层面对未来十余年疾病预防和健康促进提出了具体的行动方案。那么，健康中国行动都有哪些内容值得我们关注呢？"
    english_text = "Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes."

    link = "<a href=''>hello</a>"

    ##################### 标签
    user = "aa"


    # return render(request, "index2.html", {"name": name})
    return render(request, "index2.html", locals())

