# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0025_auto_20160211_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='taxon_order',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=14, null=True),
        ),
    ]
