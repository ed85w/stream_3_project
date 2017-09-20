# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170919_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeddingRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wedding_role', models.CharField(default=b'', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='wedding_role',
            field=models.CharField(default=b'', max_length=40),
        ),
    ]
