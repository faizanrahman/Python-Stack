from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^quotes$', views.quotes),
    url(r'^logout$', views.logout),  # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^add_quote$', views.add_quote),
    url(r'^user/(?P<id>\d+)$', views.showuser),
    url(r'^edit/(?P<id>\d+)$', views.edituser),
    url(r'^update/(?P<id>\d+)$', views.updateuser),
    url(r'^likes/(?P<id>\d+)$', views.likes),
    url(r'^delete/(?P<id>\d+)$', views.delete),
]

#(?P<id>\d+)