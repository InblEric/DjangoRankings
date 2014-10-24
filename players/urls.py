from django.conf.urls import patterns, url

from players import views

urlpatterns = patterns('',
    url(r'^$', views.pindex),
)