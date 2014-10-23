from django.conf.urls import url

from rank import views

urlpatterns = [
    url(r'^$', views.index),    
]