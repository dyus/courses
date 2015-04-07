# coding: utf-8
from django.shortcuts import render, redirect
from blog import models
from blog import forms


def posts(request):
    """ список постов """
    context = {
        'posts': models.Post.objects.all()
    }
    return render(request, 'posts.html', context)


def post_edit(request, id=None):
    c = {}

    form = forms.PostEdit(request.POST or None)
    if form.is_valid():
        post = models.Post.objects.create(
            name=form.cleaned_data.get('name'),
            article=form.cleaned_data.get('article'),
            author=form.cleaned_data.get('author')
        )
        return redirect(post_edit)

    c['form'] = form
    return render(request, 'post_edit.html', c)


def author_edit(request, id=None):
    c = {}
    form = forms.AuthorEdit(request.POST or None)
    if form.is_valid():
        author = models.Author.objects.create(
            username=form.cleaned_data.get('username'),
            last_name=form.cleaned_data.get('last_name'),
            first_name=form.cleaned_data.get('first_name')
        )
        return redirect()

    c['form'] = form
    return render(request, 'author_edit.html', c)