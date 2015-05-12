# coding: utf-8

import datetime
from django.core.urlresolvers import reverse

from django.test import TestCase

from blog import models

class BlogTestCase(TestCase):

    # def test_posts(self):
    #     url = '/super_posts/'
    #     url = reverse('blog.views.posts')
    #     response = self.client.get(url)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('test')
    #     self.assertFalse(True)

    # def test_authors(self):
    #     url = '/super_posts/'
    #     url = reverse('blog.views.posts')
    #     response = self.client.get(url)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(0)
    #     self.assertFalse(0)

    # TODO написать тест на метод модели


    def test_post_edit(self):
        author = models.Author.objects.create(username='test', last_name='test', first_name='test')
        url = reverse('blog.views.post_edit')

        self.assertFalse(models.Post.objects.exists())
        context = {
            'name': 'test_name',
            'article': 'test_article',
            'author': author.id,
            'save_post': True
        }

        response = self.client.post(url, context, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, 'http://testserver/posts/')
        if 'form' in response.context:
            self.assertFalse(response.context['form'].errors)
        self.assertTrue(models.Post.objects.exists())


    def test_post_sum(self):
        author = models.Author.objects.create(username='test', last_name='test', first_name='test')
        post = models.Post.objects.create(name=u'статья', article=u'текст', author=author)
        a = 3
        b = 4
        result = post.sum(a, b)
        self.assertEqual(7 + post.id, result)
