# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-03 14:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbelt', '0002_auto_20171203_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dob',
        ),
    ]
