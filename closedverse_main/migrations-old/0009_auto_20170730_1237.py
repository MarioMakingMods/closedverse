# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-30 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closedverse_main', '0008_auto_20170730_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirm_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='confirm_finished',
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
