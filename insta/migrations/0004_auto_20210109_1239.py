# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-09 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_auto_20210105_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_caption',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='firstname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
