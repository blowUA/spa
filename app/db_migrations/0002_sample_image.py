# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-02 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='image',
            field=models.ImageField(blank=True, help_text=b'150x150px', upload_to=b'static/img', verbose_name=b'Image link'),
        ),
    ]