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
                ('log', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=20)),
                ('time_revise', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('size_supported', models.CharField(max_length=5)),
                ('longitude', models.CharField(max_length=20)),
                ('latitude', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('balance', models.DecimalField(decimal_places=5, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to='server.User', serialize=False)),
                ('start_time', models.DateTimeField()),
                ('charge_time', models.CharField(max_length=5, default=None)),
                ('size', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('position', models.OneToOneField(primary_key=True, to='server.Position', serialize=False)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='position',
            field=models.ForeignKey(to='server.Position'),
        ),
    ]
