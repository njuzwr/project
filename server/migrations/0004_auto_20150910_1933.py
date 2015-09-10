# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('server', '0003_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(max_length=4, default=None),
        ),
    ]
