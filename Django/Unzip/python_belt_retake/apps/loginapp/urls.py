from django.conf.urls import url
from . import views         # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^wishes$', views.wishes),
    url(r'^wishes/new$', views.newWish),
    url(r'^add_wish$', views.addWish),
    url(r'^edit/(?P<id>\d+)$', views.editWish),
    url(r'^update/(?P<id>\d+)$', views.updateWish),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^granted/(?P<id>\d+)$', views.granted),
    url(r'^logout$', views.logout),  # This line has changed! Notice that urlpatterns is a list, the comma is in
]