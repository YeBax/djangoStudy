from django.shortcuts import render, HttpResponse
from django import forms
from django.forms import widgets


# Create your views here.


class UserForm(forms.Form):
    name = forms.CharField(min_length=4, label="用户名", error_messages={"required": "不能为空哦", "invalid": "格式错误了"},
                           widget=widgets.TextInput(attrs={"class": "form-control"}))
    pwd = forms.CharField(min_length=4, label="密码", widget=widgets.PasswordInput(attrs={"class": "form-control"}),
                          error_messages={"required": "不能为空哦", "invalid": "格式错误了"})
    r_pwd = forms.CharField(min_length=4, label="确认密码", widget=widgets.PasswordInput(attrs={"class": "form-control"}),
                            error_messages={"required": "不能为空哦", "invalid": "格式错误了"})
    email = forms.EmailField(label="邮箱", error_messages={"required": "不能为空哦", "invalid": "格式错误了"},
                             widget=widgets.TextInput(attrs={"class": "form-control"}))
    tel = forms.CharField(label="手机号", error_messages={"required": "不能为空哦", "invalid": "格式错误了"},
                          widget=widgets.TextInput(attrs={"class": "form-control"}))


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
            # print(form.errors)
            print(type(form.errors.get("name")))
            print(form.errors.get("name")[0])
            return render(request, "formsdemo/register.html", locals())
        '''
        if 所有的字段校验成功，则form.cleaned_data: {"name":"bai", "email": "123@q.com"}
        
        '''

    form = UserForm()  # 未绑定数据表单的对象
    return render(request, "formsdemo/register.html", locals())
