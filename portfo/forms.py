from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='نام')
    email = forms.EmailField(label='ایمیل')
    text = forms.TextInput()

    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']

class SearchForm(forms.Form):
    search = forms.CharField()
