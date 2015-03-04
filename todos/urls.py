from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^new$', 'todos.views.new_list', name='new_list'),
    url(r'^(\d+)/$', 'todos.views.view_list', name='view_list'),
    url(r'^(\d+)/add_item$', 'todos.views.add_item', name='add_item'),
)
