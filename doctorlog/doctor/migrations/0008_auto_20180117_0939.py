# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-17 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_auto_20180117_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='medicine_pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
