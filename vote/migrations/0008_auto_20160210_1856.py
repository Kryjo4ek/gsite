# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0007_votes_vote_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_text',
            field=models.TextField(verbose_name='vvedi comment'),
        ),
    ]