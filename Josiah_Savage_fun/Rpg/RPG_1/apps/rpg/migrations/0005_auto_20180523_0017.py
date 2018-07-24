# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-23 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0004_item_ranged'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='char',
            name='item',
        ),
        migrations.AddField(
            model_name='char',
            name='ranged',
            field=models.IntegerField(default=0),
        ),
    ]