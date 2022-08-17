from asyncio.windows_events import NULL # 异步IO
import json
from django.shortcuts import render, get_object_or_404
from interface.models import Tag
from django.http import HttpResponse
from forum.models import Content
import books.models as bm

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

# 回复相关
def build_comment_tree(comment_tree, commnet, num):
    comment_tree.append({})
    comment_tree[num]['u_id'] = str(commnet.u_id)
    comment_tree[num]['content'] = commnet.content
    comment_tree[num]['reply'] = []
    # print(comment_tree)
    son_commnets = commnet.comment_set.all()
    if son_commnets != None:
        cont = 0
        for son_commnet in son_commnets:
            build_comment_tree(comment_tree[num]['reply'], son_commnet, cont)
            cont += 1


def book_comment_api(request, book_id):
    """从URL获取请求的CommentID, 请求个数"""
    comments = bm.Comment.objects.filter(b_id = book_id, p_id=None)
    if comments != None:
        cont = 0
        comment_tree = []
        for comment in comments:
            build_comment_tree(comment_tree, comment, cont)
            cont+=1
        return HttpResponse(json.dumps(comment_tree))

def gsent_comment_api(request, gsent_id):
    comments = bm.Gsentence.objects.filter(p_id=gsent_id)
    if comments != None:
        cont = 0
        comment_tree = []
        for comment in comments:
            build_comment_tree(comment_tree, comment, cont)
            cont+=1
        return HttpResponse(json.dumps(comment_tree))