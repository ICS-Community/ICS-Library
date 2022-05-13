from django.conf import settings
from django.contrib.auth import models
from django.db import models
from tags.models import Tag


class Book(models.Model):
    title = models.CharField(max_length=80, verbose_name='书名') # 实际上好吧，中英文字符数量真的不好评价，回头再改吧
    cover = models.ImageField(upload_to='cover/', null=True, blank = True, verbose_name='封面') 
    author =  models.ManyToManyField(User, verbose_name='作者') # 多对多关系
    language = models.CharField(max_length=50, verbose_name='语言')
    intro = models.TextField(verbose_name='简介')
    series = models.ForeignKey('Series', verbose_name = '系列', null=True, blank = True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, verbose_name='标签') # 注意添加书籍时默认添加books标签
    if_pub = models.BooleanField(verbose_name='是否出版')
   
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return /post/pk=self.pk/
        return reverse('book', kwargs={'pk': self.pk})

class Series(models.Model):
    title = models.CharField(max_length=80, verbose_name='系列名称')
    cover = models.ImageField(upload_to='cover/', null=True, blank = True, verbose_name='封面') 
    author =  models.ManyToManyField(User, verbose_name='作者')
    language = models.CharField(max_length=50, verbose_name='语言')
    text = models.TextField(verbose_name='简介')

    def __str__(self):
        return self.title

class Starts(models.Model):
    book = models.OneToOneField(to = Book, on_delete=models.CASCADE, verbose_name='所评分的书籍')
    stars1 = models.BigIntegerField(verbose_name='一星评价')
    stars2 = models.BigIntegerField(verbose_name='二星评价')
    stars3 = models.BigIntegerField(verbose_name='三星评价')
    stars4 = models.BigIntegerField(verbose_name='四星评价')
    stars5 = models.BigIntegerField(verbose_name='五星评价')
    def __str__(self):
        return self.book.title

class Chapter(models.Model):
    b_id = models.ForeignKey('Book', verbose_name='书籍ID',on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='章节号')
    title = models.CharField(max_length=50,verbose_name='章节名')
    content = models.TextField(verbose_name='内容')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('chapter',kwargs={'pk':self.pk})

"""Publication information 出版信息"""
class Pubinfo(models.Model):
    """有的东西要改为一对多键值，回头吧"""
    b_id = models.ForeignKey('Book', verbose_name='书籍ID', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=15, verbose_name='ISBN')
    publisher = models.CharField(max_length = 20, blank = True, verbose_name='出版社')
    seller = models.CharField(max_length = 20, blank = True, verbose_name='出品方')
    otitle = models.CharField(max_length = 20, blank = True, verbose_name='原作名')
    translator =  models.ManyToManyField(User, verbose_name='译者')
    puear = models.CharField(max_length = 20, blank = True, verbose_name='出版年')
    pnum = models.CharField(max_length = 20, blank = True, verbose_name='页数')
    Price = models.CharField(max_length = 20, blank = True, verbose_name='定价')
    fram = models.CharField(max_length = 20, blank = True, verbose_name='装帧')

    def __str__(self):
        return self.isbn