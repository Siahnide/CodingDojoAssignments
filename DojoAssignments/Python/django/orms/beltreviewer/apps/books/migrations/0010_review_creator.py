# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-21 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20180521_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='creator',
            field=models.CharField(default='String', max_length=255),
            preserve_default=False,
        ),
    ]
