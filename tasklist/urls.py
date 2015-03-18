from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'todos.views.home_page', name='home'),
    url(r'^todos/', include('todos.urls')),
    url(r'^accounts/', include('accounts.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
