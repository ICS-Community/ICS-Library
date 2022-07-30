import imp
from multiprocessing.spawn import import_main_path
from django.shortcuts import render, get_object_or_404
from interface.models import Tag
from django.http import HttpResponse
from forum.models import Content
from books.models import Comment
from django.db.models import Q

def index(request):
    # 主页
    return render(request, 'forum/index.html')

def search(request):
    """搜索功能
    动态的搜索框，根据已经选择的标签，更改搜索框，比如，选择贴子之后，显示是否为仅搜索第一层。
    选择小说之后，显示字数等标签。
    """
    if request.method == 'GET':
        tags = Tag.objects.all() # 获取tags列表
        return render(request, 'interface/search.html', {'tags': tags})
    elif request.method == 'POST':
        # content = request.POST['content']
        # 获取复选框的值,是一个选中的数组
        tags = request.POST.getlist('tag_list')
        print(tags)
        content = Content.objects.filter(p_id=None) # 注意，显示所有和显示无父亲选项的作为搜索条件，可以选择。
        for tag in tags:
            content = content.filter(tags=tag)
        context = {'contents':content}
        return render(request, 'forum/forum.html', context)
        # return HttpResponse(content)

def book_comment_api(request):
    """从URL获取请求的CommentID, 请求个数"""
    f_comment = get_object_or_404(Comment, id=)
    # comments = 
    pass