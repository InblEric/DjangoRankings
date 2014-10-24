from django.conf.urls import patterns, url

from matchups import views

urlpatterns = patterns('',
    url(r'^$', views.mindex),
    url(r'^(?P<id>\d+)', views.get),    
)