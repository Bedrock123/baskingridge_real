# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-11 17:55
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaskingRidgeFiles', '0006_auto_20171209_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='news_entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
