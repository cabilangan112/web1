# Generated by Django 2.0.2 on 2018-02-11 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]