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
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}