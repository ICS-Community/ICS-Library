import imp
from multiprocessing.spawn import import_main_path
from django.shortcuts import render
from interface.models import Tag
from django.http import HttpResponse
from forum.models import Content
from django.db.models import Q

def index(request):
    # 主页
    return render(request, 'forum/index.html')

def search(request):
    if request.method == 'GET':
        tags = Tag.objects.all() # 获取tags列表
        return render(request, 'interface/search.html', {'tags': tags})
    elif request.method == 'POST':
        # content = request.POST['content']
        # 获取复选框的值,是一个选中的数组
        tags = request.POST.getlist('tag_list')
        print(tags)
        content = Content.objects.filter(p_id=None)
        for tag in tags:
            content = content.filter(tags=tag)
        context = {'contents':content}
        return render(request, 'forum/forum.html', context)
        # return HttpResponse(content)
        