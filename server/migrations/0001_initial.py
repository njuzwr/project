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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField()),
                ('log', models.CharField(max_length=100, default=None)),
                ('author', models.CharField(max_length=20, default=None)),
                ('time_revise', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stime', models.DateTimeField(default=None)),
                ('etime', models.DateTimeField(default=None)),
                ('type', models.CharField(max_length=5, default=None)),
                ('status', models.IntegerField(default=0)),
                ('charge_p', models.IntegerField(default=0)),
                ('code', models.CharField(max_length=4, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=10, default=None)),
                ('longitude', models.CharField(max_length=20)),
                ('latitude', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('balance', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='position',
            field=models.ForeignKey(to='server.Position'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.OneToOneField(to='server.User'),
        ),
    ]
