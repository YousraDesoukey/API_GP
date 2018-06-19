# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Image(models.Model):
    image = models.FileField(upload_to='media/hiero/image', blank=True, null=True)
    text = models.CharField(max_length=10000)


    def __str__(self):
        return self.text.__str__() 
