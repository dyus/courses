# coding: utf-8

from django.db import models


class Author(models.Model):
    username = models.CharField(max_length=255, verbose_name=u'Имя пользователя')
    last_name = models.CharField(max_length=255, verbose_name=u'Фамилия')
    first_name = models.CharField(max_length=255, verbose_name=u'Имя')

    def __unicode__(self):
        return u'%s %s' % (self.last_name, self.username)


class Post(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Название статьи')
    article = models.TextField(verbose_name=u'Статья')
    author = models.ForeignKey(Author, related_name=u'posts', verbose_name=u'Автор')

    def __unicode__(self):
        return u'%s %s' % (self.name, self.author)


class Comment(models.Model):
    field1 = models.CharField(max_length=255, verbose_name=u'Тествое поле')
    field2 = models.CharField(max_length=255, verbose_name=u'Тествое поле')