# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtaildocs', '0007_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('file', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wagtaildocs.Document')),
            ],
        ),
    ]