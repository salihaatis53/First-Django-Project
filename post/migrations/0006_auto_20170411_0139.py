# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 22:39
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20170410_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='metin',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
