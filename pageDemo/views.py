from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage
from app2.models import *
# Create your views here.


def index(request):
    '''
    # 批量导入
    book_list = []
    for i in range(100):
        book = Book(title="book_%s" % i, price=i*i, publishDate="2019-8-19", publish_id=1)
        book_list.append(book)
        # Book.objects.create(title="book_%s" % i, price=i*i, publishDate="2019-8-19", publish_id=1)

    Book.objects.bulk_create(book_list)
    return HttpResponse("OK")
    '''
    book_list = Book.objects.all()

    # 分页器

    paginator = Paginator(book_list, 10)
    print("count", paginator.count)  # 数据总数
    print("num_pages", paginator.num_pages)     # 总页数
    print("page_range", paginator.page_range)   # 页码列表

    try:
        page = int(request.GET.get("page"))
        current_page = paginator.page(page)

        page1 = paginator.page(1)

        # 显示某一页具体数据的两种方式
        print("object_list", page1.object_list)

        for i in page1:
            print(i)
    except EmptyPage as e:
        current_page = paginator.page(1)

    return render(request, "pagedemo/index.html", locals())

