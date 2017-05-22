# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-08 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20170508_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_act',
            name='date_time',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='add_act',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='add_act',
            name='place',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='add_act',
            name='quantity',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='add_act',
            name='register_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='add_act',
            name='speaker_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]