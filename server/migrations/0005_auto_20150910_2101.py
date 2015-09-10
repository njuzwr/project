# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('server', '0004_auto_20150910_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='charge_p',
            field=models.IntegerField(default=0),
        ),
    ]
