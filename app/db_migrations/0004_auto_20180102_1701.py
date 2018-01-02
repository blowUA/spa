# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-02 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, help_text=b'150x150px', upload_to=b'media/img/item/%Y/%m/%d', verbose_name=b'Image link'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='image',
            field=models.ImageField(blank=True, help_text=b'150x150px', upload_to=b'media/img/sample/%Y/%m/%d', verbose_name=b'Image link'),
        ),
    ]