# coding: utf8
from django.db import models


# Create your models here.

class Host(models.Model):
    HostName = models.CharField(max_length=256)
    IP = models.IPAddressField()

    class Meta:
        verbose_name_plural = "主机表"
