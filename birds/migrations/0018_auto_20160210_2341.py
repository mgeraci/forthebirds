# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-11 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0017_auto_20160210_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='en_IOC',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='species',
            name='report_as',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
