from django.contrib import admin

# Register your models here.
from web import models


class HostInfoAdmin(admin.ModelAdmin):
    list_display = ('HostName', 'IP')


admin.site.register(models.Host,HostInfoAdmin)
