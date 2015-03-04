from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'todos.views.home_page', name='home'),
    url(r'^todos/the-only-todo-list-in-the-world/$', 'todos.views.view_list', name='view_list'),
    url(r'^todos/new$', 'todos.views.new_list', name='new_list')
    #url(r'^admin/', include(admin.site.urls)),
)
