# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 11:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to=b'avatars')),
                ('group', models.CharField(blank=True, max_length=8)),
                ('sub_group', models.IntegerField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('date_joined', models.DateField()),
                ('about', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
