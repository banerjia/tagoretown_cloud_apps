# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 21:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_auto_20170130_2041'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerAddress',
            new_name='Address',
        ),
    ]