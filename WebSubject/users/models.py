from django.conf import settings
from django.db import models
from books.models import Book
from django.contrib.auth.models import User
from interface.models import Tag

class Profile(models.Model):
    # 个人信息相关，头像之类的。
    u_id = models.OneToOneField(to = User, on_delete=models.CASCADE, verbose_name="用户ID")
    nickname = models.CharField(max_length=90, verbose_name="昵称")
    points = models.BigIntegerField(default = 0, verbose_name="积分")
    
    def __str__(self):
        return self.u_id.username

class Bookshelf(models.Model):
    title = models.CharField(max_length=50,verbose_name='书架名称')
    u_id = models.ForeignKey(User, verbose_name='所有者', null=True, blank = True, on_delete=models.SET_NULL)
    intro = models.CharField(verbose_name='书架简介', max_length=256, null=True, blank = True) 

    def __str__(self):
        return (self.title + ' - ' + self.u_id.username)

class Bookforbs(models.Model):
    """用于存储书架上的书籍"""
    f_id = models.ForeignKey('Bookshelf', verbose_name='指向书架的id', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name='书籍ID', null=True, blank = True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return (self.book.title + ' - ' + self.f_id.__str__())
    
class Status(models.Model):
    """用于记录一些日常状态"""
    u_id = models.OneToOneField(to = User, on_delete=models.CASCADE, verbose_name="用户ID")
    check_in_time = models.DateField( null=True, blank = True, verbose_name="最后签到日期")
    Continuous_check_in_time = models.IntegerField(default = 0, verbose_name="连续签到时间")
    check_in_points = models.IntegerField(default = 0, verbose_name="签到获取的积分")

    def __str__(self):
        return self.u_id.username
