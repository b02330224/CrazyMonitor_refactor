# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-15 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0018_auto_20160525_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='host_alive_check_interval',
            field=models.IntegerField(default=30, verbose_name='\u4e3b\u673a\u5b58\u6d3b\u72b6\u6001\u68c0\u6d4b\u95f4\u9694'),
        ),
    ]