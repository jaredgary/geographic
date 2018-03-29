# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(active=True)


# Create your models here.
class Country(models.Model):
    CODES_CHOICES = (('CO','Colombia'), ('USA','EEAA'), ('MX', 'Mexico'))
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3, choices=CODES_CHOICES)
    continent = models.ForeignKey('continents.Continent', on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)
    active_manager = ActiveManager()
    objects = models.Manager()

    def __str__(self):
        return self.name