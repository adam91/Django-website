# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 17:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20160215_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='website.Continent'),
        ),
    ]
