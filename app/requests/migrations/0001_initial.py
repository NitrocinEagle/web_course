# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-05 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='\u0418\u043c\u044f')),
                ('group', models.CharField(max_length=256, verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f')),
                ('email', models.CharField(max_length=60, verbose_name='\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u0430\u0434\u0440\u0435\u0441')),
                ('social', models.CharField(max_length=60, verbose_name='\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0432 \u0441\u043e\u0446. \u0441\u0435\u0442\u044f\u0445')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
