# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-17 13:43
from __future__ import unicode_literals

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20171217_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='conten',
            field=ckeditor.fields.RichTextField(default='\u8270\u82e6\u597d\u7a7a\u95f4'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cont',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name=b'\xe8\x89\xb0\xe8\x8b\xa6\xe5\xa5\xbd\xe7\xa9\xba\xe9\x97\xb4'),
        ),
    ]
