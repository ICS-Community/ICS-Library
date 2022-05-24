from django import forms
from .models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'intro', 'tags', 'content']
        labels = {'title':'标题', 'intro':'简介', 'tags':'标签', 'content':'正文'}
        widgets = {'content': forms.Textarea(attrs={'cols':80})}