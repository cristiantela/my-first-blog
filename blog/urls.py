from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='teste'),
	url(r'^post/new/$', views.post_new_edit, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_new_edit, name='post_edit'),
]