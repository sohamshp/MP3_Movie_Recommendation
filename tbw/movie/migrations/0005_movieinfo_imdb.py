# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-28 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_unrated'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='imdb',
            field=models.CharField(default='', max_length=20),
        ),
    ]
