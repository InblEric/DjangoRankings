from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^players/', include('players.urls')),
	url(r'^matchups/', include('matchups.urls')),		
	url(r'^$', include('rank.urls')),
)
