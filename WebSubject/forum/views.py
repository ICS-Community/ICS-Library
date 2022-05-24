from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


def index(request):
    # 主页
    return render(request, 'forum/index.html')

def forum(request):
    # 社区首页
    contents = Content.objects.all()
    # 对于每一个 帖子，如果有 intro = 
    context = {'contents':contents}
    return render(request, 'forum/forum.html', context)

def topic_detail(request, topic_id):
    topic = get_object_or_404(Content, id=topic_id)
    tags = topic.tags.all().order_by('title')
    context = {'topic':topic, 'tags':tags}
    return render(request, 'forum/topic_detail.html', context)

# @login_required
def add_topic(request):
    '''添加新的帖子'''
    # 检查所有权
    # 根据？传参确定是全新的帖子还是回复帖子。

    if request.method != 'POST':
        # 未提交数据，创建一个新表单
        form = TopicForm()

    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            # 在前端强制选中帖子标签Javascript实现
            new_topic.save()
            return HttpResponseRedirect(reverse('forum:topic_detail',args=[new_topic.id]))
    
    context = {'form':form}
    return render(request, 'forum/add_topic.html', context)

# @login_required
def edit_topic(request, topic_id):
    '''编辑既有章节'''
    topic = get_object_or_404(Content, id=topic_id)
    # check_topic_owner(topic, request)

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = TopicForm(instance=topic)
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('forum:topic_detail',args=[topic_id]))
    
    context = {'topic': topic, 'form': form}
    return render(request, 'forum/edit_topic.html', context)