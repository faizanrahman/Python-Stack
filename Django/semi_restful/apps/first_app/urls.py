from django.conf.urls import url
from . import views           # This line is new!
import re
urlpatterns = [
    url(r'^users$', views.index),   # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^users/new$', views.new),
    url(r'^users/(?P<id>\d+)/edit$', views.update),
    url(r'^users/(?P<id>\d+)/delete$', views.delete),
    url(r'^users/(?P<id>\d+)$', views.show),
    url(r'^users/create$', views.create),
    url(r'^users/update$', views.updated),
] 