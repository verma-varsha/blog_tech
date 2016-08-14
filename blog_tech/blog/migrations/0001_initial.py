# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-14 02:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CommentUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=150)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=150)),
                ('post_content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
            ],
        ),
        migrations.AddField(
            model_name='commentuser',
            name='user_post',
            field=models.ManyToManyField(to='blog.Post'),
        ),
    ]
