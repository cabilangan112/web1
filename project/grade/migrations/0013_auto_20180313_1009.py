# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-13 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0012_auto_20180313_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='First_year_Grade',
            field=models.BooleanField(default=False),
        ),
    ]
