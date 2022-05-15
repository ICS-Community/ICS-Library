from django.conf import settings
from django.db import models
from books.models import Book

class Index(models.Model):
    """首页书籍展示表"""
    plate = models.IntegerField(verbose_name='板块编号')
    number = models.IntegerField(verbose_name='在该板块的编号')
    b_id = models.ForeignKey('books.Book', verbose_name='书籍ID',on_delete=models.CASCADE)
    r_text = models.TextField(verbose_name='推荐语')

# 组织表-书社
class Organize(models.Model):
    o_id = models.CharField(verbose_name="组织ID", unique=True, max_length=20)
    """要一个访问限制"""

# 帖子表 用于社区的书单，帖子，书籍的长回复
class Topic(models.Model):
    # t_id = models.CharField(verbose_name='帖子id', max_length=16)
    t_uid = models.CharField(verbose_name='帖子所属用户id', max_length=16)
    t_kind = models.CharField(verbose_name='类别', max_length=32)
    create_time = models.DateField(verbose_name='创建时间', auto_now_add=True)
    t_photo = models.CharField(verbose_name='帖子图片', max_length=128, null=True)
    t_content = models.CharField(verbose_name='帖子正文', max_length=3000)
    t_title = models.CharField(verbose_name='帖子标题', max_length=64)
    t_introduce = models.CharField(verbose_name='帖子简介', max_length=256)
    recommend = models.BooleanField(verbose_name='是否推荐', default=False)

# 回复表
class Reply(models.Model):
    r_tid = models.CharField(verbose_name='帖子id', max_length=16)
    r_uid = models.CharField(verbose_name='发表者id', max_length=16)
    r_photo = models.CharField(verbose_name='回复的图片', max_length=128, null=True)
    r_time = models.DateField(verbose_name='留言时间', auto_now_add=True)
    r_content = models.CharField(verbose_name='回复内容', max_length=256)