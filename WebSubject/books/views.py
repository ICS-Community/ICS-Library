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
    authors = book.author.all().order_by('username')
    tags = book.tags.all().order_by('title')
    series = None
    if book.series != None:
        series = book.series
    if(len(chapters)==0):
        la_chapter = 0
    else:
        la_chapter = chapters[len(chapters)-1]
    context = {'book':book, 'authors':authors, 'series':series, 'chapters':chapters, 'tags':tags, 'la_chapter':la_chapter,}
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

@login_required
def add_book(request):
    '''添加新的书籍'''
    # 检查所有权

    if request.method != 'POST':
        # 未提交数据，创建一个新表单
        form = BookForm()

    else:
        # POST提交的数据，对数据进行处理
        form = BookForm(data=request.POST)
        if form.is_valid():
            new_book = form.save(commit=False)
            # 在前端强制选中书籍标签Javascript实现
            # b_tag = Tag.objects.get(tid=books)
            # new_book.tags.add(b_tag)
            new_book.save()
            return HttpResponseRedirect(reverse('books:book_detail',args=[new_book.id]))
    
    context = {'book':new_book, 'form':form}
    return render(request, 'books/add_book.html', context)

@login_required
def edit_book(request, book_id):
    '''编辑既有书籍'''
    book = get_object_or_404(Book, id=book_id)
    # check_topic_owner(topic, request)

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = BookForm(instance=book)
    else:
        # POST提交的数据，对数据进行处理
        form = BookForm(instance=book, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('books:book_detail',args=[book_id]))
    
    context = {'book': book, 'form': form}
    return render(request, 'books/edit_book.html', context)

@login_required
def add_chapter(request, book_id):
    '''在特定的书籍中添加新的章节'''
    book = get_object_or_404(Book, id=book_id)
    # 检查所有权

    if request.method != 'POST':
        # 未提交数据，创建一个新表单
        form = ChapterForm()

    else:
        # POST提交的数据，对数据进行处理
        form = ChapterForm(data=request.POST)
        if form.is_valid():
            new_chapter = form.save(commit=False)
            new_chapter.b_id = book
            new_chapter.number = book.latest_c_num + 1
            book.latest_c_num = new_chapter.number
            book.save()
            new_chapter.save()
            return HttpResponseRedirect(reverse('books:book_detail',args=[book_id]))
    
    context = {'book':book, 'form':form}
    return render(request, 'books/add_chapter.html', context)

@login_required
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


