# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20171022_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
