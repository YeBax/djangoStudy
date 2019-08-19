from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage
from app2.models import *

import random
# Create your views here.


def index(request):

    book_list = Book.objects.all()

    # 分页器

    paginator = Paginator(book_list, 5)
    print("count", paginator.count)  # 数据总数
    print("num_pages", paginator.num_pages)     # 总页数
    print("page_range", paginator.page_range)   # 页码列表

    page = int(request.GET.get("page"))

    if paginator.num_pages > 11:
        # 动态效果 分页器   最多展示 11个页码
        if page - 5 < 1:
            page_range = range(1, 12)   # 前 11个
        elif page + 5 > paginator.num_pages:
            page_range = range(paginator.num_pages - 10, paginator.num_pages + 1)   # 最后 11个
        else:
            page_range = range(page-5, page+6)  # 中间情况
    else:
        page_range = paginator.page_range

    try:
        current_page = paginator.page(page)

        page1 = paginator.page(1)

        # 显示某一页具体数据的两种方式
        print("object_list", page1.object_list)

        for i in page1:
            print(i)
    except Exception as e:
        page = 1
        current_page = paginator.page(1)
    # except EmptyPage:
    #     page = 1
    #     current_page = paginator.page(1)

    return render(request, "pagedemo/index.html", locals())


def bulk_books(request):
    # 批量导入
    book_list = [
        Book(title="book_%s" % i, price=random.randint(0.0, 500.0), publishDate="2019-8-20", publish_id=1) for i in range(1000)
    ]
    # for i in range(100):
        # book = Book(title="book_%s" % i, price=i*i, publishDate="2019-8-19", publish_id=1)
        # book_list.append(book)
        # Book.objects.create(title="book_%s" % i, price=i*i, publishDate="2019-8-19", publish_id=1)

    Book.objects.bulk_create(book_list)

    return HttpResponse("OK")

