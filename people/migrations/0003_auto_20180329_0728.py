# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-29 13:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_person_father'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='father',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.Person'),
        ),
    ]
