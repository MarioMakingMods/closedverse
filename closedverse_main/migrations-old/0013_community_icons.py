# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-30 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closedverse_main', '0012_auto_20170730_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='icons',
            field=models.URLField(blank=True),
        ),
    ]
