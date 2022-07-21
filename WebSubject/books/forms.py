from django import forms
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author','language', 'series', 'intro', 'tags', 'if_pub']
        labels = {'title':'书名', 'author':'作者','language':'语言', 'series':'系列', 'intro':'简介', 'tags':'标签', 'if_pub':'是否出版'}

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'content']
        labels = {'title':'章节名称', 'content':'章节内容'}
        widgets = {'content': forms.Textarea(attrs={'cols':80})}

class GsentenceForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content':'好句'}
        widgets = {'content':forms.Textarea(attrs={'cols':80})}

# class ShortcommentForm(froms.ModelForm):
#     class Meta:
