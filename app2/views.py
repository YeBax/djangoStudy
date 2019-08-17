# coding:utf-8
from django.shortcuts import render, HttpResponse
from django.urls import reverse
# Create your views here.
from .models import *


def index(request):
    url = reverse("app2:index")
    print(url)
    return HttpResponse("index2 OK")


def login(request):

    return render(request, "login.html")


def orders(request):
    return render(request, "orders.html")


def query(request):
    """
    跨表查询：
        1 基于对象查询
        2 基于双下划线查询
        3 聚合和分组查询
        4 F 与 Q 查询
    :param request:
    :return:
    """
    # ------------------- 基于对象的跨表查询（子查询）----------------------

    # 一对多查询的正向查询： 查询金瓶梅这本书的出版社的名字

    # book_obj = Book.objects.filter(title="金瓶梅").first()
    #
    # print(book_obj.publish)  # 与这本书关联出版社对象
    # print(book_obj.publish.name)

    # 一对多查询的反向查询： 查询人民出版社 出版过的书籍名称
    # publish = Publish.objects.filter(name="人民出版社").first()
    # ret = publish.book_set.all()
    # print(ret)

    # 多对多查询的正向查询：查询金瓶梅 所有作者的名字
    # book_obj = Book.objects.filter(title="金瓶梅").first()
    # author_list = book_obj.authors.all()  # queryset对象  [author1, author2, author3 ...]
    # for author in author_list:
    #     print(author.name)

    # 多对多查询的反向查询：查询 。。。 出版过的所有书籍名称
    # author = Author.objects.filter(name="柏杉同学").first()
    # book_list = author.book_set    .all()
    # print(book_list)
    # for book in book_list:
    #     print(book.title, book.publish)

    # 一对一查询 正向查询：查询zzz的手机号
    # xiao = Author.objects.filter(name="小呆").first()
    # print(xiao.authorDetail.telephone)

    # 一对一查询的反向查询：查询手机号18600000000的作者名字和年龄
    # ad = AuthorDetail.objects.filter(telephone="18600000000").first()
    # print(ad.author.name)
    # print(ad.author.age)

    # ------------------- 基于双下划线的跨表查询（join查询）----------------------
    # 一对多查询的正向查询： 查询金瓶梅这本书的出版社的名字
    '''
    # select app2_publish.name from app2_book inner join app2_publish
    # on app2_book.publish_id = app2_publish.nid
    # where app2_book.title="金瓶梅";
    '''
    # 正向查询按字段，反向查询按表明小写 来告诉ORM引擎join那张表
    # ret = Book.objects.filter(title="金瓶梅").values("publish__name")


    # 方式2
    # ret = Publish.objects.filter(book__title="金瓶梅").values("name")

    #  多对多查询：查询金瓶梅 所有作者的名字
    #
    # 方式1
    # 需求 通过book表join与其关联的author表，属于正向查询，按字段author通知ORM引擎join book_author 与 author_book
    # ret = Book.objects.filter(title="金瓶梅").values('authors__name')

    # 方式2：
    # 需求 通过author表join与其关联的book表，属于反向查询：按表名小写book通知ORM引擎join book_author 与 book
    # ret = Author.objects.filter(book__title="金瓶梅").values("name")

    # 一对一查询的正向查询：查询 小呆 手机号
    # 方式1：
    # 需求 通过book表join与其关联的authorDetail表，属于正向查询，按字段authorDetail 通知ORM引擎join authorDetail表
    ret = Author.objects.filter(name="小呆").values('authorDetail__telephone')

    # 方式2：通过authorDetail表join与其关联的Author表，属于反向查询，按表名小写通知ORM引擎join Author表
    AuthorDetail.objects.filter(author__name="小呆").values('telephone')

    # 进阶联系
    # 练习 手机号以170开头 的作者出版过的所有书籍名称 以及 书籍出版社的名称
    # 方式1
    # 需求 通过book表join与AuthorDetail表，Book与AuthorDetail无关联，所以必须连续跨表
    # ret = Book.objects.filter(authors__authorDetail__telephone__startswith="170").values("title", "publish__name")

    # 方式2
    # ret1 = Author.objects.filter(authorDetail__telephone__startswith="170").values_list("book__title", "book__publish__name")
    #
    # print(ret)
    # print(ret1)

    # ------------------- 集合与分组查询----------------------
    # ---------------------------聚合  aggregate:返回值是一个字典，不再是 queryset
    # 查询所有书籍的平均价格
    from django.db.models import Avg, Max, Min, Count

    # ret = Book.objects.all().aggregate(avg_price=Avg("price"))
    # print(ret) # {'avg_price': Decimal('39.966667')}

    ret = Book.objects.all().aggregate(avg_price=Avg("price"), max_price=Max("price"))
    print(ret) # {'avg_price': Decimal('39.966667'), 'max_price': Decimal('50.60')}

    return HttpResponse("OK\t\r<h1>hello world</h1>")
'''
A-B
关联属性在A表中
正向查询: A ---> B
反向查询：B ---> A

# 一对多查询0  
    正向查询：按字段
    反向查询：按表名  表名小写_set
    
    book_obj.publish
    Book 关联属性：publish ------> publish
                          <------
    publish_obj.book_set.all() # queryset
    
# 多对多查询
    正向查询：按字段
    反向查询：按表名  表名小写_set.all()
    
    book_obj.authors.all()
    Book 关联属性：Author对象 ------> Author
                        <------
    author_obj.book_set.all() # queryset
    

# 一对一查询
    正向查询：按字段
    反向查询：表名小写
    
    author.authordetail
    Author对象 关联属性：authordetail ------> AuthorDetail 对象
                        <------
    authordetail.author # queryset 
    
    
基于双下划线的跨表查询(join查询)
    key:正向查询按字段，反向查询按表明小写



'''
