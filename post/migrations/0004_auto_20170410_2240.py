# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20170410_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='metin',
            field=models.TextField(verbose_name='Yazı'),
        ),
    ]
