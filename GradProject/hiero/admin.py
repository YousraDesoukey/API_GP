# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_filter = ('image', 'text')
    search_fields = ['image', 'text']
    list_display = ['image', 'text']


admin.site.register(Image,ImageAdmin)
