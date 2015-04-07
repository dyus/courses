from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^posts/', 'blog.views.posts'),
    url(r'^post_edit/', 'blog.views.post_edit'),
    url(r'^author_edit/', 'blog.views.author_edit'),
    url(r'^author_edit/(\d+)/', 'blog.views.author_edit'),
    # url(r'^authors/', 'blog.views.authors'),
)
