# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantongbbs', '0002_auto_20160721_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='PTagPrice',
            field=models.CharField(choices=[('50以下', '50以下'), ('50-100', '50-100'), ('100-300', '100-300'), ('300以上', '300以上')], max_length=50),
        ),
    ]
