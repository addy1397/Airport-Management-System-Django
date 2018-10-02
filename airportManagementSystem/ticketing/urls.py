from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<iD>[0-9]+)/$', views.detail, name='detail'),
    url(r'^book/$', views.book, name='book'),
    url(r'^(?P<iD>[0-9]+)/cancel/$', views.cancel, name='cancel'),
    url(r'^(?P<iD>[0-9]+)/ticket/$', views.ticket, name='ticket'),
    #url(r'^confirm/$', views.confirm, name='confirm'),
    url(r'^confirm/(?P<start>\w+)/(?P<des>\w+)/(?P<id>[0-9]+)/$', views.confirm, name='confirm'),
]
