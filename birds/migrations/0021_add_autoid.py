# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0020_remove_minnesotaspecies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
