from django.db import models
from books.models import Book

class Tag(models.Model):
    id = models.CharField(max_length=30, verbose_name='标签ID') # 必要性？
    tid = models.CharField(max_length=30, verbose_name='标签识别名') # 英文识别名，唯一，用于网站路径
    # 对 Book，帖子建立多对多关系。
    # book = models.ManyToManyField(Publication) #

    def __str__(self):
        return self.tagname

    def get_absolute_url(self):
        # return /post/pk=self.pk/
        return reverse('booklist', kwargs={'pk': self.pk})
