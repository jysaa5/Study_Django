# from django import forms
from django.forms import ModelForm
from second.models import Post
from django.utils.translation import gettext_lazy as _ # static한 문자열을 선언할 때 사용

# class PostForm(forms.Form):
#     # title = forms.CharField(label="제목", max_length=200)
#     title = forms.CharField(label="제목", max_length=10)
#     content = forms.CharField(label="내용", widget=forms.Textarea)

class PostForm(ModelForm):
    class Mata:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': _('제목'),
            'content': _('내용'),
        }
