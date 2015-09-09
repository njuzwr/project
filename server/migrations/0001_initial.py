# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseVersion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('version', models.IntegerField()),
                ('log', models.CharField(max_length=100, default=None)),
                ('author', models.CharField(max_length=20, default=None)),
                ('time_revise', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('type', models.CharField(max_length=10, default=None)),
                ('longitude', models.CharField(max_length=20)),
                ('latitude', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('user', models.OneToOneField(primary_key=True, default=None, to='server.User', serialize=False)),
                ('stime', models.DateTimeField(default=None)),
                ('etime', models.DateTimeField(default=None)),
                ('type', models.CharField(max_length=5, default=None)),
                ('status', models.IntegerField(default=0)),
                ('charge_p', models.CharField(max_length=5, default=None)),
                ('position', models.ForeignKey(to='server.Position')),
            ],
        ),
    ]
