from django.conf import settings
from django.db import models
from books.models import Book
from django.contrib.auth.models import User
from tags.models import Tag

class Profile(models.Model):
    # 个人信息相关，头像之类的。
    nickname = models.CharField(max_length=90, verbose_name="昵称")

class Bookshelf(models.Model):
    f_id = models.ForeignKey('Bookshelf', verbose_name='指向书架的id', null=True, blank = True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50,verbose_name='书架名称')
    b_id = models.ForeignKey(Book, verbose_name='书籍ID',on_delete=models.CASCADE)
    u_id = models.ForeignKey(User, verbose_name='所有者', null=True, blank = True, on_delete=models.SET_NULL)
    intro = models.CharField(verbose_name='书架简介', max_length=256, null=True, blank = True) 

    def __str__(self):
        return self.title
    
