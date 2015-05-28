from django.conf.urls import patterns, include, url
from . import views
from xcel import settings

urlpatterns = patterns('',
	url(r'^new/$', views.post_new, name='new'),
	url(r'^$', views.main, name='main'),
)
