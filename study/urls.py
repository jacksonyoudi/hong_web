from django.conf.urls import include, url
from views import index,login

urlpatterns = [

    url(r'index/', index),
    url(r'login/', login),
]