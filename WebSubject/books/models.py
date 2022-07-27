from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from interface.models import Tag


class Book(models.Model):
    # 实际上好吧，中英文字符数量真的不好评价，回头再改吧
    title = models.CharField(max_length=80, verbose_name='书名')
    cover = models.ImageField(upload_to='cover/', null=True, blank = True, verbose_name='封面') 
    author =  models.ManyToManyField(User, verbose_name='作者') # 多对多关系
    language = models.CharField(max_length=50, verbose_name='语言')
    intro = models.TextField(verbose_name='简介')
    series = models.ForeignKey('Series', verbose_name = '系列', null=True, blank = True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, verbose_name='标签') # 注意添加书籍时默认添加books标签
    latest_c_num = models.IntegerField(verbose_name='最新章节号', default=0)
    if_pub = models.BooleanField(verbose_name='是否出版')
    Related_Information = models.TextField(verbose_name="相关信息", null=True, blank = True)
   
    def __str__(self):
        return self.title

class Series(models.Model):
    title = models.CharField(max_length=80, verbose_name='系列名称')
    cover = models.ImageField(upload_to='cover/', null=True, blank = True, verbose_name='封面') 
    author =  models.ManyToManyField(User, verbose_name='作者')
    language = models.CharField(max_length=50, verbose_name='语言')
    text = models.TextField(verbose_name='简介')

    def __str__(self):
        return self.title

class Starts(models.Model):
    b_id = models.OneToOneField(to = Book, on_delete=models.CASCADE, verbose_name='所评分的书籍')
    stars0 = models.BigIntegerField(verbose_name='零星评价', default=0)
    stars1 = models.BigIntegerField(verbose_name='一星评价', default=0)
    stars2 = models.BigIntegerField(verbose_name='二星评价', default=0)
    stars3 = models.BigIntegerField(verbose_name='三星评价', default=0)
    stars4 = models.BigIntegerField(verbose_name='四星评价', default=0)
    stars5 = models.BigIntegerField(verbose_name='五星评价', default=0)
    stars6 = models.BigIntegerField(verbose_name='六星评价', default=0)
    stars7 = models.BigIntegerField(verbose_name='七星评价', default=0)
    stars8 = models.BigIntegerField(verbose_name='八星评价', default=0)
    stars9 = models.BigIntegerField(verbose_name='九星评价', default=0)
    stars10 = models.BigIntegerField(verbose_name='十星评价', default=0)
    def __str__(self):
        return self.b_id.title


"""
建立一个新的模型，用于存储目录结构。
"""

class Section(models.Model):
    '''小说分卷，分节信息'''
    b_id = models.ForeignKey('Book', verbose_name='分节信息', on_delete=models.CASCADE)


class Chapter(models.Model):
    b_id = models.ForeignKey('Book', verbose_name='书籍ID', on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='章节号')
    title = models.CharField(max_length=50,verbose_name='章节名')
    content = models.TextField(verbose_name='内容')

    def __str__(self):
        return self.title

class Gsentence(models.Model):
    p_id = models.ForeignKey('Gsentence', verbose_name='指向内容的id', null=True, blank = True, on_delete=models.SET_NULL)
    # 没指向内容的是好句，有的是评论
    b_id = models.ForeignKey('Book', verbose_name='书籍ID', on_delete=models.CASCADE)
    u_id = models.ForeignKey(User, verbose_name="用户ID", null=True, blank=True, on_delete=models.SET_NULL)
    content = models.TextField(verbose_name='内容')

    def __str__(self):
        return self.b_id.title

class Comment(models.Model):
    """和 Gsentence 非常相似"""
    p_id = models.ForeignKey('Comment', verbose_name='指向内容的id', null=True, blank = True, on_delete=models.SET_NULL)
    b_id = models.ForeignKey("Book", verbose_name="书籍ID", on_delete=models.CASCADE)
    u_id = models.ForeignKey(User, verbose_name="用户ID", null=True, blank=True, on_delete=models.SET_NULL)
    content = models.TextField(verbose_name='内容')

    def __str__(self):
        return self.b_id.title



"""Publication information 出版信息"""
class Pubinfo(models.Model):
    """有的东西要改为一对多键值，回头吧"""
    b_id = models.ForeignKey('Book', verbose_name='书籍ID', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=15, verbose_name='ISBN')
    content = models.TextField(verbose_name='内容')
    # 所有以下内容均用前端语法渲染实现
    # publisher = models.CharField(max_length = 20, blank = True, verbose_name='出版社')
    # seller = models.CharField(max_length = 20, blank = True, verbose_name='出品方')
    # otitle = models.CharField(max_length = 20, blank = True, verbose_name='原作名')
    # translator =  models.ManyToManyField(User, verbose_name='译者')
    # puear = models.CharField(max_length = 20, blank = True, verbose_name='出版年')
    # pnum = models.CharField(max_length = 20, blank = True, verbose_name='页数')
    # Price = models.CharField(max_length = 20, blank = True, verbose_name='定价')
    # fram = models.CharField(max_length = 20, blank = True, verbose_name='装帧')
    def __str__(self):
        return self.isbn

