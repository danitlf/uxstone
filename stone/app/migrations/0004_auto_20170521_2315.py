# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-22 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170521_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='version',
            name='descricao',
        ),
        migrations.AlterField(
            model_name='projeto',
            name='descricao',
            field=models.TextField(blank=True, max_length=100, verbose_name='descri\xe7\xe3o'),
        ),
    ]