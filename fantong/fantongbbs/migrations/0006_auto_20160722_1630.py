# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantongbbs', '0005_auto_20160722_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbspost',
            name='PTime',
            field=models.DateTimeField(null=True),
        ),
    ]
