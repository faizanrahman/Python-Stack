from django.conf.urls import url
from django.utils.crypto import get_random_string
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),   # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^random_word$', views.random),
    url(r'^random_word/reset$', views.reset)
]   