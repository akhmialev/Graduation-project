from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class AddNews(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput,
            'slug': forms.TextInput,
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

class UserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput)
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'text')