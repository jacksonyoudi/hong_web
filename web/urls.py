# coding: utf8
from django.conf.urls import include, url
from views import ajax, index, add, server
from django.contrib.auth.models import User
from models import Host
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('url', 'HostName', 'IP')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'hosts', HostViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'ajax/', ajax),
    url(r'server/', server),
    url(r'index/(?P<page>\d*)', index),
    url(r'add/', add),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
