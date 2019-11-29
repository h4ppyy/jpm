from django import forms
from .models import Post, PostMemory


class PostForm(forms.Form):
    title = forms.CharField(
      widget=forms.TextInput(attrs={'class': 'form-control'}),
      label='제목',
      label_suffix='',
      help_text=''
    )
    content = forms.CharField(
      widget=forms.Textarea(attrs={'class': 'form-control'}),
      label='내용',
      label_suffix='',
      help_text=''
    )
    