# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-25 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]