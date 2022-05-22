from django import forms
from .models import *

# class TopicForm(forms.ModelForm):
#     class Meta:
#         model = Topic
#         fields = ['text']
#         labels = {'text':''}

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['content']
        labels = {'content':'章节'}
        widgets = {'content': forms.Textarea(attrs={'cols':80})}