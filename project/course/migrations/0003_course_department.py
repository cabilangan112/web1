# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-05 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.department'),
        ),
    ]
