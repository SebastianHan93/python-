from django.forms import widgets
from django import forms
from blog.models import UserInfo
from django.core.exceptions import ValidationError

class UserForm(forms.Form):
    user = forms.CharField(max_length=32,label="用户名",error_messages={"required":"该字段不能为空"},widget=widgets.TextInput(attrs={"class":"form-control"},))
    pwd = forms.CharField(max_length=32,label="密码",widget=widgets.PasswordInput(attrs={"class":"form-control"},))
    re_pwd = forms.CharField(max_length=32,label="再次输入密码",widget = widgets.PasswordInput(attrs={"class":"form-control"}))
    email = forms.EmailField(max_length=32,label="邮箱",widget = widgets.EmailInput(attrs={"class":"form-control"}))

    def clean_user(self):
        temp_user = self.cleaned_data.get("user")
        user = UserInfo.objects.filter(username = temp_user).first()
        if not user:
            return temp_user
        else:
            raise ValidationError("用户名已存在")

    def clean(self):
        pwd = self.cleaned_data.get("pwd")
        re_pwd = self.cleaned_data.get("re_pwd")
        print("pwd:%s,rePwd:%s" % (pwd, re_pwd))
        print("111++++++24b")
        if pwd and re_pwd:
            if pwd == re_pwd:
                print("111++++++24")
                return self.cleaned_data
            else:

                raise ValidationError("两次密码不一致")
        else:
            return self.cleaned_data