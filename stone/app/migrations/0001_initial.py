# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.TextField(blank=True, max_length=1000, verbose_name='Mudan\xe7a Feita')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='uploads', verbose_name='Foto:')),
                ('nome', models.TextField(blank=True, max_length=100, verbose_name='Nome')),
                ('cargo', models.TextField(blank=True, max_length=100, verbose_name='Cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='uploads', verbose_name='Imagem:')),
                ('nome', models.TextField(blank=True, max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(blank=True, max_length=100, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Versoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('versao', models.CharField(blank=True, max_length=100, null=True, verbose_name='Numero da Vers\xe3o')),
                ('titulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='titulo')),
                ('descricao', models.TextField(blank=True, max_length=1000, verbose_name='descricao')),
                ('data', models.DateTimeField(auto_now=True)),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Projeto')),
            ],
        ),
        migrations.AddField(
            model_name='features',
            name='versao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Versoes'),
        ),
    ]
