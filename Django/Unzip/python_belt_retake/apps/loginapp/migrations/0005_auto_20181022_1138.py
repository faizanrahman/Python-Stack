# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-22 16:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0004_auto_20181022_1137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wish',
            old_name='desc',
            new_name='description',
        ),
    ]
