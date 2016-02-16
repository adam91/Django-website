# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20160215_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='about',
            field=models.TextField(default='City', max_length=1000),
        ),
        migrations.AlterField(
            model_name='city',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/photos'),
        ),
        migrations.AlterField(
            model_name='country',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
