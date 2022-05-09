from django.db import models

class Book(models.Model):
    id = models.CharField(max_length=20, verbose_name = '书籍ID', primary_key=True) # 采用52进制， 并设为主键
    title = models.CharField(max_length=80, verbose_name='书名') # 实际上好吧，中英文字符数量真的不好评价，回头再改吧
    ISBN = models.CharField(max_length=15, blank = True, verbose_name='ISBN')
    cover = models.ImageField(upload_to='cover/',verbose_name='封面') 
    author = models.CharField(max_length=50, verbose_name='作者')
    lanuge = models.CharField(max_length=50, Verbose_name='语言')
    """
    出版社: 浙江文艺出版社
    出品方: KEY·可以文化
    原作名: Gra na wielu bębenkach
    译者: 茅银辉 / 方晨
    出版年: 2021-9
    页数: 390
    定价: 66.00元
    装帧: 平装
    丛书: 奥尔加·托卡尔丘克作品
    # 我不确定这样一个部分是否应当使用json来写。。。 ！！！！！
    """
    intro = models.TextField(verbose_name='简介')
    stars1 = models.BigIntegerField(verbose_name='一星评价')
    stars2 = models.BigIntegerField(verbose_name='二星评价')
    stars3 = models.BigIntegerField(verbose_name='三星评价')
    stars4 = models.BigIntegerField(verbose_name='四星评价')
    stars5 = models.BigIntegerField(verbose_name='五星评价')
    # tag = models.ManyToManyField(Publication) # 多对多关系建立

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return /post/pk=self.pk/
        return reverse('book', kwargs={'pk': self.pk})


class Chapter(models.Model):
    number = models.IntegerField(verbose_name='章节号')
    title = models.CharField(max_length=50,verbose_name='章节名')
    content = models.TextField(verbose_name='内容')
    b_id = models.ForeignKey('Book', verbose_name='书籍ID',on_delete=models.CASCADE) # 章节所对的书籍的ID

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('chapter',kwargs={'pk':self.pk})
