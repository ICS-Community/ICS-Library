from django import forms
from .models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'intro', 'tags', 'text']
        labels = {'title':'标题', 'intro':'简介', 'tags':'标签', 'text':'正文'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}