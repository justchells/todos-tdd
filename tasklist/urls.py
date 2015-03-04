from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'todos.views.home_page', name='home'),
    url(r'^todos/new$', 'todos.views.new_list', name='new_list'),
    url(r'^todos/(\d+)/$', 'todos.views.view_list', name='view_list'),
    url(r'^todos/(\d+)/add_item$', 'todos.views.add_item', name='add_item')
    #url(r'^admin/', include(admin.site.urls)),
)
