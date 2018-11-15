# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-15 03:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupDetail',
            fields=[
                ('detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(null=True)),
                ('end_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'group_detail',
            },
        ),
        migrations.CreateModel(
            name='GroupInfo',
            fields=[
                ('info_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('img', models.CharField(max_length=100)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('count', models.IntegerField()),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'group_info',
            },
        ),
        migrations.AddField(
            model_name='groupdetail',
            name='info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.GroupInfo'),
        ),
    ]