from django.conf import settings
from django.db import models
from books.models import Book
from django.contrib.auth.models import User
from interface.models import Tag

class Index(models.Model):
    """首页书籍展示表"""
    plate = models.IntegerField(verbose_name='板块编号')
    number = models.IntegerField(verbose_name='在该板块的编号')
    book = models.ForeignKey('books.Book', verbose_name='书籍ID',on_delete=models.CASCADE)
    r_text = models.TextField(verbose_name='推荐语')

# 组织表-书社
class Organize(models.Model):
    o_id = models.CharField(verbose_name="组织ID", unique=True, max_length=20)
    """要一个访问限制"""

# 帖子表 用于社区的书单，帖子，书籍的长回复
class Content(models.Model):
    p_id = models.ForeignKey('Content', verbose_name='指向内容的id', null=True, blank = True, on_delete=models.SET_NULL) 
    author =  models.ForeignKey(User, verbose_name='作者', null=True, blank = True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, verbose_name='标签') # 注意,帖子，专栏，书单就是用这个来分类的哒。
    create_time = models.DateField(verbose_name='创建时间', auto_now_add=True)
    # t_photo = models.CharField(verbose_name='帖子图片', max_length=128, null=True)
    text = models.CharField(verbose_name='正文', max_length=3000)
    title = models.CharField(verbose_name='标题', max_length=64)
    intro = models.CharField(verbose_name='内容摘要', max_length=256, null=True, blank = True) # 如果为空的话就默认使用内容前五十个字符。

    def __str__(self):
        return self.title
    
    # 定义一个函数返回内容的前50个字符
    def ffchar(self):
        return self.text[:50]

# 回复表
class Reply(models.Model):
    r_tid = models.CharField(verbose_name='帖子id', max_length=16)
    r_uid = models.CharField(verbose_name='发表者id', max_length=16)
    # r_photo = models.CharField(verbose_name='回复的图片', max_length=128, null=True)
    r_time = models.DateField(verbose_name='留言时间', auto_now_add=True)
    r_content = models.CharField(verbose_name='回复内容', max_length=256)