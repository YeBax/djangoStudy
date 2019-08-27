from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, render, redirect
from luffydemo import settings
from django.contrib.auth.decorators import login_required


class CustomerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("CustomerMiddleware process -requests-...")
        # return HttpResponse("被拦截了。。。。")

    def process_response(self, request, response):
        print("CustomerMiddleware process *response*...")
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("callback==>", callback)
        print("callback_args==>", callback_args)
        print("callback_kwargs==>", callback_kwargs)
        print("CustomerMiddleware1 process_view")
        # ret = callback(callback_args)
        # return ret

    def process_exception(self, request, exception):
        print("CustomerMiddleware1 process exception....")

class CustomerMiddleware2(MiddlewareMixin):
    def process_request(self, request):
        print("CustomerMiddleware2 process -requests-...")

    def process_response(self, request, response):
        print("CustomerMiddleware2 process *response*...")
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("CustomerMiddleware2 process_view")

    def process_exception(self, request, exception):
        print("CustomerMiddleware2 process exception....")
        return HttpResponse(exception)


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(request.META['REMOTE_ADDR'])
        white_list = settings.WHITER_LIST
        if request.path in white_list:
            return None     # 通过校验，不写return 和 写return None 中间件效果一样 ，往下执行

        if not request.user.is_authenticated:
            return redirect("/authdemo/login/")