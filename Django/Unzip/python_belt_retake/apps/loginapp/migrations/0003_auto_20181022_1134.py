# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-22 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0002_wish'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wish',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
