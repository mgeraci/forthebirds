# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-15 02:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0074_remove_speakingprogramfile_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speakingprogramfile',
            name='program',
        ),
        migrations.DeleteModel(
            name='SpeakingProgramFile',
        ),
    ]