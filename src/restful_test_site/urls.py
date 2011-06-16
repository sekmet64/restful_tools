from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restful_tools.views.home', name='home'),
    # url(r'^restful_tools/', include('restful_tools.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^restful_test/$', 'restful_test_app.views.index'),
    url(r'^restful_test/bookshelves/(?P<bookshelf>\w*)/?(?P<book>\w*)$', 'restful_test_app.views.api'),
    url(r'^restful_test/books/(?P<book>\w*)$', 'restful_test_app.views.books')
)
