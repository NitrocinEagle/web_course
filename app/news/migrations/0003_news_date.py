# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-22 15:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20160303_0454'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 3, 22, 15, 39, 53, 607046, tzinfo=utc)),
            preserve_default=False,
        ),
    ]