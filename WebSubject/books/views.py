from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# from .tools import check_topic_owner, check_topic_public


# Create your views here.
def index(request):
    '''Library主页'''
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'books/index.html', context)

def book_detail(request, book_id):
    '''显示书籍的详细信息'''
    book = get_object_or_404(Book, id=book_id)
    chapters = book.chapter_set.order_by('number')
    tags = book.tags.all().order_by('title')
    context = {'book':book, 'chapters':chapters, 'tags':tags}
    return render(request, 'books/book.html', context)

def series_detail(request, series_id):
    '''显示系列的详细信息'''
    series = get_object_or_404(Series, id=series_id)
    books = series.book_set.order_by('title')
    context = {'series':series, 'books':books}
    return render(request, 'books/series.html', context)

def chapter(request, book_id, chapter_id):
    '''显示章节内容'''
    book = get_object_or_404(Book, id=book_id)
    chapter = get_object_or_404(Chapter, id=chapter_id)
    context = {'book':book, 'chapter':chapter}
    return render(request, 'books/chapter.html', context)

# @login_required
def edit_chapter(request, book_id, chapter_id):
    '''编辑既有章节'''
    chapter = get_object_or_404(Chapter, id=chapter_id)
    book = get_object_or_404(Book, id=book_id)
    # check_topic_owner(topic, request)

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = ChapterForm(instance=chapter)
    else:
        # POST提交的数据，对数据进行处理
        form = ChapterForm(instance=chapter, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('books:book_detail',args=[book_id]))
    
    context = {'chapter': chapter, 'book': book, 'form': form}
    return render(request, 'books/edit_chapter.html', context)



# def search(request):
#     '''搜索页'''
#     return render(request, 'books/search.html')


# @login_required
# def new_topic(request):
#     '''添加新主题'''
#     if request.method != 'POST':
#         # 未提交数据：创建一个新表单
#         form = TopicForm()
#     else:
#         # POST提交的数据，对数据进行处理
#         form = TopicForm(request.POST)
#         if form.is_valid():
#             new_topic = form.save(commit=False)
#             new_topic.owner = request.user
#             if request.POST.get('dropdown',None) == 'Public':
#                 new_topic.public = True

#             new_topic.save()
#             return HttpResponseRedirect(reverse('learning_logs:topics'))

#     context={'form':form}
#     return render(request, 'books/index.html', context)

# @login_required
# def new_entry(request, topic_id):
#     '''在特定的主题中添加新条目'''
#     topic = Topic.objects.get(id=topic_id)
#     check_topic_owner(topic, request)

#     if request.method != 'POST':
#         # 未提交数据，创建一个新表单
#         form = EntryForm()

#     else:
#         # POST提交的数据，对数据进行处理
#         form = EntryForm(data=request.POST)
#         if form.is_valid():
#             new_entry = form.save(commit=False)
#             new_entry.topic = topic
#             new_entry.save()
#             return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
    
#     context = {'topic':topic, 'form':form}
#     return render(request, 'books/index.html', context)


# @login_required
# def my_topics(request):
#     '''显示用户个人所有的主题'''

#     topics = Topic.objects.filter(owner=request.user, topic_hide=False).order_by('date_added')
#     context = {'topics':topics}
#     return render(request, 'books/index.html', context)

# @login_required
# def delete_entry(request, entry_id):
#     '''删除选定条目'''
#     entry = Entry.objects.get(id=entry_id)
#     topic = entry.topic
#     check_topic_owner(topic, request)
#     entry.entry_hide = True
#     entry.save()

#     return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))

# @login_required
# def delete_topic(request, topic_id):
#     '''删除选定主题'''
#     topic = Topic.objects.get(id=topic_id)
#     check_topic_owner(topic, request)
#     topic.topic_hide = True
#     topic.save()
    
#     return HttpResponseRedirect(reverse('learning_logs:my_topics'))