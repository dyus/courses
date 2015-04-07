# coding: utf-8
from django import forms
from blog import models


class PostEdit(forms.Form):
    name = forms.CharField(label=u'Название')
    article = forms.CharField(label=u'Статья', widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=models.Author.objects.all())


class AuthorEdit(forms.Form):
    username = forms.CharField(label=u'Логин')
    last_name = forms.CharField(label=u'Фамилия')
    first_name = forms.CharField(label=u'Имя')
