# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 00:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0012_species_main_sound_recording'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='minnesotaspecies',
            name='miscellaneous_notes',
        ),
        migrations.RemoveField(
            model_name='minnesotaspecies',
            name='range_in_minnesota',
        ),
    ]
