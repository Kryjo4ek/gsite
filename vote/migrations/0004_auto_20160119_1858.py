# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0003_remove_vote_total_number_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote_enumerator',
            field=models.IntegerField(null=True),
        ),
    ]