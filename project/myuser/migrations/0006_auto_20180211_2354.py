# Generated by Django 2.0.2 on 2018-02-11 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0005_auto_20180211_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='MI',
            field=models.CharField(default=1, help_text='Enter your middle Name', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='Sex',
            field=models.CharField(blank=True, choices=[('m', 'Male'), ('o', 'Female')], default='m', max_length=1),
        ),
    ]
