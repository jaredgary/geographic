# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=255)
    nacionality = models.ManyToManyField('countries.Country')
    father = models.OneToOneField('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    def __str__(self):
        return self.first_name