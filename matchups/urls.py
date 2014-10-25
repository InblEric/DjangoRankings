from django.conf.urls import patterns, url

from matchups import views

urlpatterns = patterns('',
    url(r'^$', views.mindex),
	url(r'^(?P<id>\d+)/vote1', views.vote1),    
	url(r'^(?P<id>\d+)/vote2', views.vote2),    	
	url(r'^(?P<id>\d+)', views.get),    
)