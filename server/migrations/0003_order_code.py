# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('server', '0002_auto_20150909_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='code',
            field=models.IntegerField(default=0),
        ),
    ]
