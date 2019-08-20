from django import forms


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

    def clean_name(self):
        val = self.cleaned_data.get("name")
        ret = UserInfo.objects.filter(name=val)
        if not ret:
            return val
        else:
            raise ValidationError("该用户已经注册！")

    def clean_tel(self):
        val = self.cleaned_data.get("tel")  # 当局部钩子没有通过校验，不会走到这一步，直接抛异常。这一定有tel字段
        if len(val) == 11:
            return val
        else:
            raise ValidationError("手机号格式错误！")

    def clean(self):
        pwd = self.cleaned_data.get("pwd")
        r_pwd = self.cleaned_data.get("r_pwd")
        if r_pwd and pwd:
            if pwd == r_pwd:
                return self.cleaned_data
            else:
                raise ValidationError("两次密码不一致")
        else:
            return self.cleaned_data
