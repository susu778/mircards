from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# 引入该应用的数据库表
from .models import User
# from .models import User


def index(request):
    test = "success"
    return render(request, 'ams/index.html', {"test": test})


def browse(request):
    test_str = "this is browse page."
    return render(request, 'ams/browse.html', {"test": test_str})


def login(request):
    return render(request, 'ams/login.html',)


def login1(request):
    return render(request, 'ams/login1.html')


def login2(request):
    return render(request, 'ams/login2.html')


def userlogin(request):
    # 获取用户通过表单post方式传过来的参数，括号中的参数是表单元素的name
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 提前设置好提示语
    fail_user = "用户不存在！"
    fail_psw = "密码错误！"
    # 首先判断用户名是否存在，exist()返回值是True或False
    flag = User.objects.using('local').filter(user_name=username).exists()
    # 如果用户存在，就进一步判断对应的密码是否匹配
    if flag:
        # 查询数据库，获取这个用户的信息
        query_res = User.objects.using('local').get(user_name=username)
        # 判断用户的密码是否匹配，匹配的话，就跳转到首页
        if query_res.user_psw == password:
            # 如果页面有其他数据要从数据库获取，那就获取他们，一起返回给前台模板
            query_set = User.objects.using('local').all()
            return render(request, 'ams/index.html',{'result':query_res,'data': query_set})
        # 如果密码不匹配，则在login页面显示“密码错误！”的提示信息
        else:
            return render(request, 'ams/login.html', {'fail_str': fail_psw})
    # 如果用户不存在，则在login页面显示“用户不存在！”的提示信息
    else:
        return render(request, 'ams/login.html', {'fail_str': fail_user})
