# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-13 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.CharField(default='this is a descripriton', max_length=255),
            preserve_default=False,
        ),
    ]