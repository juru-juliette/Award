# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-10-30 09:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='pic/')),
                ('bio', models.TextField()),
                ('phone_number', models.CharField(max_length=50)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pic/')),
                ('description', tinymce.models.HTMLField()),
                ('link', models.CharField(max_length=200)),
                ('view_grade', models.IntegerField(null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='award.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.IntegerField()),
                ('usability', models.IntegerField()),
                ('content', models.IntegerField()),
                ('total', models.IntegerField()),
                ('avg', models.IntegerField(null=True)),
                ('comment', models.TextField(null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='award.Project')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
