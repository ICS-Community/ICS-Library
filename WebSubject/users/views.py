from django.views.generic import View
# django自带用户类
from django.contrib.auth.models import User
from django.shortcuts import redirect, reverse, render, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages # 为什么消息提示发送在管理页面？
from django.utils import timezone
from .models import *
from django.http import HttpResponse

class check_in(View):
    def get(self, request):
        user = request.user
        status = user.status
        d1 = timezone.now().strftime("%Y-%m-%d")
        if str(status.check_in_time) != d1: # 如果今天还没有签到
            status.check_in_time = d1
            status.save()
            # return HttpResponse(status.check_in_time)
            context = {'user': user, 'sign_in_status':0}
            return render(request, 'users/check_in.html', context)
        else:
            # return HttpResponse('ok')
            context = {'user': user, 'sign_in_status':1}
            return render(request, 'users/check_in.html', context)
    def post(self, request):
        pass

def User_detail(request, u_id):
    user = get_object_or_404(User, id=u_id)
    profile = user.profile
    u_bfs = user.bookshelf_set.order_by('title')  # 你的所有书架
    context = {'user': user, 'profile': profile, 'u_bfs': u_bfs}
    return render(request, 'users/user_detail.html', context)


def Book_list(request, u_id, bf_id):
    bf = get_object_or_404(Bookshelf, id=bf_id)
    books = bf.bookforbs_set.order_by('book')
    context = {'bf': bf, 'books': books}
    return render(request, 'users/book_list.html', context)

def User_manage(request, u_id):
    user = get_object_or_404(User, id=u_id)
    profile = user.profile
    context = {'user': user, 'profile': profile}
    return render(request, 'users/user_manage.html', context)

# 注册
class Register(View):

    def get(self, request):
        # 检测用户已登录过点击注册则跳转主页，注销才能重新注册，会保存15分钟登录状态
        if request.user.is_authenticated:
            return redirect(reverse('forum:index'))
        return render(request, 'users/register.html')

    def post(self, request):
        # 注册
        username = request.POST.get('username', '')  # 用户名
        password = request.POST.get('password', '')  # 密码
        check_password = request.POST.get('check_password', '')  # 确认密码

        # 检测密码与确认密码一致
        if password != check_password:
            messages.success(request, "密码不一致")
            return redirect(reverse('users:register'))

        # 检测是否为空
        if username == '' or password == '' or check_password == '':
            messages.success(request, "不能为空!")
            return redirect(reverse('users:register'))

        # 检测当前账号是否注册过并提示用户
        exists = User.objects.filter(username=username).exists()
        if exists:
            messages.success(request, "该账号已注册!")
            return redirect(reverse('users:register'))
        new_user = User.objects.create_user(username=username, password=password)
        new_user.save()
        u_profile = Profile.objects.create(u_id=new_user, nickname=username)
        u_profile.save()
        u_status = Status.objects.create(u_id=new_user)
        u_status.save()
        login(request, new_user)
        return redirect(reverse('forum:index'))

# 登录
class Login(View):

    def get(self, request):
        # 检测用户已登录过点击注册则跳转主页，注销才能重新登录，会保存15分钟登录状态
        if request.user.is_authenticated:
            return redirect(reverse('forum:index'))
        return render(request, 'users/login.html')

    def post(self, request):
        # 登录
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # 判断当前用户是否存在,不存在则重新注册
        exists = User.objects.filter(username=username).exists()
        if not exists:
            messages.success(request, "该账号不存在，请重新注册!")
            return redirect(reverse('users:login'))

        # 检测是否为空
        if username == '' or password == '':
            messages.success(request, "不能为空!")
            return redirect(reverse('users:login'))

        # 验证账号密码正确
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('forum:index'))
        else:
            messages.success(request, "密码错误")
            return redirect(reverse('users:login'))


def Logout(request):
    logout(request)
    return redirect(reverse('forum:index'))
