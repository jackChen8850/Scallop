# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-05 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scallop', '0007_auto_20171105_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondtype',
            name='url',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='secondtype',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='申请表具体类型'),
        ),
    ]
