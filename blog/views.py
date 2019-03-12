from django.shortcuts import render,HttpResponse
from blog.utils import validCode


from django.http import JsonResponse
from django.contrib import auth
from blog.format_form import UserForm
from django.forms import forms
from blog.models import UserInfo


# Create your views here.
#登陆页面
def login(request):

    if request.method=="POST":
        response = {"user":None,"msg":None}
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        valid_code = request.POST.get("valid_code")
        valid_code_str = request.session.get("valid_code_str")
        print(valid_code_str,"-----")
        if valid_code.upper() == valid_code_str.upper():
            user = auth.authenticate(username=user,password=pwd)
            if user:
                auth.login(request,user) #request.user = 当前登陆对象
                response["user"] = user.username
            else:
                response["msg"] = "username or password error!"
        else:
            response["msg"]="valid code error"
        return JsonResponse(response)


    return render(request, "blog/login.html")

#获取登陆验证图片
def get_validCode_img(request):
    img = validCode.get_valid_code_img(request)
    return  HttpResponse(img)

#主页
def index(request):
    return render(request, "blog/index.html")


#注册页面x
def register(request):
    if request.is_ajax():
        print(request.POST)
        form = UserForm(request.POST)
        #user当作一个标志位
        response = {"user":None,"msg":None}
        if form.is_valid():
            response["user"] = form.cleaned_data.get("user")
            #生成一条用户纪录
            user = form.cleaned_data.get("user")
            pwd = form.cleaned_data.get("pwd")
            email = form.cleaned_data.get("email")
            avatar_obj = request.FILES.get("avatar")
            #添加纪录
            if avatar_obj:
                UserInfo.objects.create_user(username=user,password=pwd,email = email,avatar = avatar_obj)
            else:
                UserInfo.objects.create_user(username=user,password=pwd,email = email)
        else:
            print(form.cleaned_data)
            print(form.errors)
            response["msg"] = form.errors


        return  JsonResponse(response)

    form = UserForm()

    return render(request,"blog/register.html",{"form":form})
