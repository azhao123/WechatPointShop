# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-17 13:47
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20171217_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cont',
        ),
        migrations.RemoveField(
            model_name='product',
            name='conten',
        ),
        migrations.AlterField(
            model_name='product',
            name='content',
            field=ckeditor.fields.RichTextField(default=b''),
        ),
    ]