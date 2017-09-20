# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170919_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='wedding_role',
            field=models.CharField(default=b'', max_length=15, blank=True, choices=[(b'bride', b'BRIDE'), (b'groom', b'GROOM'), (b'mother of bride', b'MOTHER OF BRIDE'), (b'mother of groom', b'MOTHER OF GROOM'), (b'maid of honor', b'MAID OF HONOR'), (b'bridesmaid', b'BRIDESMAID'), (b'best man', b'BEST MAN')]),
        ),
        migrations.DeleteModel(
            name='WeddingRole',
        ),
    ]
