# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-14 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_content_short',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
