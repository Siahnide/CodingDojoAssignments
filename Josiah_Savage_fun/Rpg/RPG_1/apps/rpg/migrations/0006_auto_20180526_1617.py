# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-26 23:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpg', '0005_auto_20180523_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='char',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='item',
        ),
        migrations.AddField(
            model_name='char',
            name='arms_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='arms', to='rpg.Item'),
        ),
        migrations.AddField(
            model_name='char',
            name='both_hands_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='both_hands', to='rpg.Item'),
        ),
        migrations.AddField(
            model_name='char',
            name='chest_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='chest', to='rpg.Item'),
        ),
        migrations.AddField(
            model_name='char',
            name='feet_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='feet', to='rpg.Item'),
        ),
        migrations.AddField(
            model_name='char',
            name='head_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='head', to='rpg.Item'),
        ),
        migrations.AddField(
            model_name='char',
            name='left_hand_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='left_hand', to='rpg.Item'),
        ),
        migrations.AddField(
            model_name='char',
            name='right_hand_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='right_hand', to='rpg.Item'),
        ),
        migrations.DeleteModel(
            name='Equipment',
        ),
    ]
