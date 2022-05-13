from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # 主页
    return render(request, 'forum/index.html')
