# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 19:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0028_remove_species_report_as'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='species',
            options={'ordering': ['taxon_order'], 'verbose_name_plural': 'bird species'},
        ),
    ]
