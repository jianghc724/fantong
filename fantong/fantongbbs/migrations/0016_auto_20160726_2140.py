# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantongbbs', '0015_auto_20160726_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbspost',
            name='PReplyNum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bbspost',
            name='PTop',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bbspost',
            name='PVisitNum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bbsuser',
            name='UNickname',
            field=models.TextField(blank=True),
        ),
    ]
