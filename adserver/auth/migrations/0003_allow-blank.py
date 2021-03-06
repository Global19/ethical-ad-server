# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-05 23:19
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('adserver_auth', '0002_publisher-advertiser-adtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='advertisers',
            field=models.ManyToManyField(blank=True, to='adserver.Advertiser'),
        ),
        migrations.AlterField(
            model_name='user',
            name='publishers',
            field=models.ManyToManyField(blank=True, to='adserver.Publisher'),
        ),
    ]
