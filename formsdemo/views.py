from django.shortcuts import render, HttpResponse
from formsdemo.myforms import *

from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
# Create your views here.


def reg(request):
    if request.method == "POST":
        # form = UserForm({"name":"bai", "email": "123@q.com"})
        print(request.POST)
        form = UserForm(request.POST)  # form表单的那么属性值应该与forms组件字段名称一致·
        print(form.is_valid())  # 返回布尔值

        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.cleaned_data)
            print(form.errors)
            # print(type(form.errors.get("name")))
            # print(form.errors.get("name")[0])

            # 全局钩子错误
            print(form.errors.get("__all__")[0])
            r_pwd_error = form.errors.get("__all__")
            return render(request, "formsdemo/register.html", locals())
        '''
        if 所有的字段校验成功，则form.cleaned_data: {"name":"bai", "email": "123@q.com"}
        
        '''

    form = UserForm()  # 未绑定数据表单的对象
    return render(request, "formsdemo/register.html", locals())
