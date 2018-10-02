from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<iD>[0-9]+)/$', views.detail, name='detail'),
    url(r'^book/$', views.book, name='book'),
    url(r'^(?P<iD>[0-9]+)/cancel/$', views.cancel, name='cancel'),
]
