import imp
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .tools import *
from interface.models import Tag
from books.models import Book


def index(request):
    # 主页
    return render(request, 'forum/index.html')

def forum(request):
    # 社区首页
    contents = Content.objects.filter(p_id=None)
    context = {'contents':contents}
    return render(request, 'forum/forum.html', context)

def topic_detail(request, topic_id):
    topic = get_object_or_404(Content, id=topic_id)
    tags = topic.tags.all().order_by('title')
    # 楼主贴下发帖功能 JS 实现
    Follow_topics = topic.content_set.order_by('create_time')
    context = {'topic':topic, 'tags':tags, 'Follow_topics':Follow_topics}
    return render(request, 'forum/topic_detail.html', context)

@login_required
def add_topic(request, topic_id=-1):
    '''添加新的楼主帖子'''
    # 检查所有权

    if request.method != 'POST':
        # 未提交数据，创建一个新表单
        form = TopicForm()

    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save()
            new_topic.author = request.user
            # 在前端强制选中帖子标签Javascript实现
            if topic_id == -1:
                new_topic.save()
                return HttpResponseRedirect(reverse('forum:topic_detail',args=[new_topic.id]))
            else:
                new_topic.p_id = get_object_or_404(Content, id=topic_id)
                new_topic.save()
                return HttpResponseRedirect(reverse('forum:topic_detail',args=[topic_id]))
    
    context = {'topic_id':topic_id, 'form':form}
    return render(request, 'forum/add_topic.html', context)

@login_required
def edit_topic(request, topic_id):
    '''编辑既有帖子'''
    topic = get_object_or_404(Content, id=topic_id)
    check_topic_owner(topic, request)

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = TopicForm(instance=topic)
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            if topic.p_id == None:
                return HttpResponseRedirect(reverse('forum:topic_detail',args=[topic_id]))
            else:
                return HttpResponseRedirect(reverse('forum:topic_detail',args=[topic.p_id.id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'forum/edit_topic.html', context)

def tag_detail(request, tid):
    """标签详情页面, 注意参考Pixiv"""
    tag = get_object_or_404(Tag, tid=tid)
    # 特判，几个重定向
    if tid == 'book': return redirect(reverse('books:index'))
    # 获取几个不同内容
    books = Book.objects.filter(tags=tag)
    context = {'tag':tag, 'books':books}
    return render(request, 'forum/tag_detail.html', context)