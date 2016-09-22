from django.conf.urls import include, url
from views import ajax, index, add

urlpatterns = [

    url(r'ajax/', ajax),
    url(r'index/(?P<page>\d*)', index),
    url(r'add/', add),
]
