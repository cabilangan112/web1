# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-13 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0009_auto_20180313_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='First_year_Grade',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')]),
        ),
    ]
