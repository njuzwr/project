# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('server', '0002_auto_20150911_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='charge_p',
            field=models.IntegerField(default=10),
        ),
    ]
