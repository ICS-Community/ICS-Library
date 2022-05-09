from django.db import models

class Book(models.Model):
    id = models.CharField(max_length=20, verbose_name = '书籍ID', primary_key=True) # 采用52进制， 并设为主键
    title = models.CharField(max_length=80, verbose_name='书名') # 实际上好吧，中英文字符数量真的不好评价，回头再改吧
    cover = models.ImageField(upload_to='cover/',verbose_name='封面') 
    author = models.CharField(max_length=50, verbose_name='作者')
    intro = models.TextField(verbose_name='简介')
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
    book = models.ForeignKey('Book',verbose_name='书名',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('chapter',kwargs={'pk':self.pk})
